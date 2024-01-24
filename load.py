#!/usr/bin/env python
from doris.doris import load_species, save_species, Specy

def update(specy):
    """
    Update the object here
    """
    pass


def update_all():
    # species = load_species('/srv/volumes/bio.yaml', remote_load=False)
    (species, tags) = load_species('/home/francois/species2.yaml', remote_load=False)
    for specy in species.values():
        update(specy)
    # save_species('/home/francois/species2.yaml', species, [])


def load_one(stdout=True):
    data = {
        'name': 'Antiopelle',
        'inpn': 547264,
        'doris': 335
    }
    specy = Specy.from_dict(data, remote_load=True)
    if (stdout):
        print(specy.dump())
    else:
        save_species('/tmp/species2.yaml', {specy.id: specy}, [])


if __name__ == '__main__':
    load_one()
