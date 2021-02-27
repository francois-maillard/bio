# Run the tests

```bash
pip install -r requirements.txt
pytest tests/
```

# Run locally

```bash
pip install -r requirements.txt
python -m doris
```

# Run as a docker image

```bash
docker build -t bio .
docker run -ti bio -d
```

# Global vars

* `$PORT` the port number on which the servers binds
* `$CONFIG` the path of the yaml file describing the species

# Update data after adding a new feature

```python
from doris.doris import load_species, save_species

def update(specy):
    """
    Update the object here
    """

species = load_species('/srv/volumes/bio.yaml', remote_load=False)
for specy in species.values():
    update(specy)
save_species('/home/francois/species.yaml', species)
```
