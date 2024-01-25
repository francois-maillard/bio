import logging
import os
import random
from typing import Dict, Tuple, List
from flask import Flask, render_template, abort, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash
from .doris import Specy, load_species, save_species

logging.basicConfig(level=logging.INFO)


APP_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_STATIC = os.path.join(APP_ROOT, "static")
APP_TPL = os.path.join(APP_ROOT, "templates")
USERNAME = 'doris'
PASSWORD = 'pbkdf2:sha256:150000$7tSG9wVB$6099ec2ffd43f16604f1e75ff497c826cc2548853b8f947eee4593ab81de9004'
FILENAME = os.environ.get('CONFIG',
                          os.path.join(APP_ROOT, 'species.yaml'))

# pylint: disable=invalid-name
app = Flask(__name__)
auth = HTTPBasicAuth()


(SPECIES, TAGS) = load_species(FILENAME, remote_load=False)


@auth.verify_password
def verify_password(username: str, password: str) -> str:
    if username == USERNAME and \
           check_password_hash(PASSWORD, password):
        return username


def filter_species() -> Tuple[Dict, List]:
    tags = request.args.getlist('tags')
    if tags is not None and len(tags) != 0:
        return ({specy.id: specy for specy in SPECIES.values() if set(specy.tags) & set(tags)}, tags)
    return (SPECIES, tags)


@app.route("/")
@app.route("/species")
def list_species() -> str:
    """ Species page """
    (species, tags) = filter_species()
    return render_template("species.html.j2", page="species",
                           species=species, tags=tags, all_tags=TAGS)


@app.route("/species/random")
def random_specy() -> str:
    (species, tags) = filter_species()
    specy = random.choice(list(species.values()))
    photo = random.choice(specy.photos)
    return render_template("specy.html.j2", page="random",
                           specy=specy,
                           photo=photo,
                           tags=tags,
                           all_tags=TAGS,
                           hidden=True)


@app.route("/species/<specy_id>", methods=['DELETE'])
@auth.login_required
def delete_specy(specy_id: int) -> str:
    specy_id = int(specy_id)
    if specy_id not in SPECIES:
        abort(404)
    del SPECIES[specy_id]
    save_species(FILENAME, SPECIES, TAGS)
    return '', 204
  

@app.route("/species/<specy_id>", methods=['GET'])
def show_specy(specy_id: int) -> str:
    specy_id = int(specy_id)
    if specy_id not in SPECIES:
        abort(404)
    return render_template("specy.html.j2", page="specy",
                           specy=SPECIES[specy_id])


@app.route("/species/<specy_id>/photos/<photo_id>", methods=['DELETE'])
@auth.login_required
def delete_photo(specy_id: int, photo_id: int) -> str:
    specy_id = int(specy_id)
    if specy_id not in SPECIES:
        abort(404)
    specy = SPECIES[specy_id]

    photo_id = int(photo_id)
    if photo_id > len(specy.photos) - 1 or photo_id < 0:
        abort(404)

    del specy.photos[photo_id]
    save_species(FILENAME, SPECIES, TAGS)
    return '{}', 204


@app.route("/species/<specy_id>/thumbnail", methods=['POST'])
@auth.login_required
def specy_thumbnail(specy_id: int) -> str:
    specy_id = int(specy_id)
    if specy_id not in SPECIES:
        abort(404)
    specy = SPECIES[specy_id]

    photo_id = int(request.json.get('photo_id'))
    if photo_id > len(specy.photos) - 1 or photo_id < 0:
        abort(404)

    specy.thumbnail = specy.photos[photo_id]['url']
    specy.image = specy.photos[photo_id]['url']
    save_species(FILENAME, SPECIES, TAGS)
    return '{}', 201


@app.route("/species/new")
@auth.login_required
def create_specy() -> str:
    global SPECIES
    data = {}
    message = {}
    created = False
    specy = None
    new_specy = None

    data['specy'] = request.args.get('specy', None)
    data['inpn'] = request.args.get('inpn', None)
    data['doris'] = request.args.get('doris', None)
    data['name'] = request.args.get('name', None)
    if data['doris']:
        data['doris'] = int(str(data['doris']).split('/')[-1])
    if data['inpn']:
        data['inpn'] = int(data['inpn'])

    if request.args.get('create'):
        created = True

    if data['specy'] or data['inpn']:
        try:
            specy = Specy.from_dict(data, remote_load=True)
        except KeyError as exc:
            message = {'level': 'danger',
                       'message': f'{exc.__class__.__name__}: {str(exc)}'}
        except AssertionError:
            message = {'level': 'danger', 'message': 'Non trouvé'}

    if specy:
        if specy.id in SPECIES:
            message = {'level': 'danger',
                       'message': f'{specy.name} existe déjà'}
        elif created:
            # Save
            SPECIES[specy.id] = specy
            save_species(FILENAME, SPECIES, TAGS)

            # Message
            message = {'level': 'success',
                       'message': f'{specy.name} a été ajoutée'}

            # Reset form data
            new_specy = specy
            specy = None
            data = {}
    else:
        specy = None
    return render_template("specy_create.html.j2",
                           specy=specy,
                           new_specy=new_specy,
                           data=data,
                           message=message,
                           page="specy_create")
