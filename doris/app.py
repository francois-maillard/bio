import logging
import os
from flask import Flask, render_template, abort, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash
from .doris import Specy, load_species, save_specy

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


SPECIES = load_species(FILENAME)


@auth.verify_password
def verify_password(username: str, password: str) -> str:
    if username == USERNAME and \
           check_password_hash(PASSWORD, password):
        return username


@app.route("/")
@app.route("/species")
def list_species() -> str:
    """ Species page """
    return render_template("species.html.j2", page="species",
                           species=SPECIES)


@app.route("/species/<specy_id>")
def show_specy(specy_id: int) -> str:
    specy_id = int(specy_id)
    if specy_id not in SPECIES:
        abort(404)
    return render_template("specy.html.j2", page="specy",
                           specy=SPECIES[specy_id])


@app.route("/species/new")
@auth.login_required
def create_specy() -> str:
    global SPECIES
    data = {}
    message = {}
    created = False
    specy = None

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
            specy = Specy.from_dict(data)
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
            save_specy(FILENAME, data)

            # Reload data
            SPECIES = load_species(FILENAME)

            # Message
            message = {'level': 'success',
                       'message': f'{specy.name} a été ajoutée'}

            # Reset form data
            specy = None
            data = {}
    else:
        specy = None
    return render_template("specy_create.html.j2",
                           specy=specy, data=data,
                           message=message,
                           page="specy_create")
