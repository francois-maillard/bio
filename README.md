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
