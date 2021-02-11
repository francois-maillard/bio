import logging
import os
from flask import Flask, render_template, abort
from .doris import Specy, load_species

logging.basicConfig(level=logging.INFO)


APP_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_STATIC = os.path.join(APP_ROOT, "static")
APP_TPL = os.path.join(APP_ROOT, "templates")
FILENAME = os.environ.get('CONFIG',
                          os.path.join(APP_ROOT, 'species.yaml'))

# pylint: disable=invalid-name
app = Flask(__name__)


SPECIES = load_species(FILENAME)


@app.route("/")
@app.route("/species")
def list_species() -> str:
    """ Species page """
    return render_template("index.html", page="species",
                           species=SPECIES)
