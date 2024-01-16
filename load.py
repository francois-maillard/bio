from doris.doris import load_species, save_species, Specy

def update(specy):
    """
    Update the object here
    """
    pass


def update_all():
    species = load_species('/srv/volumes/bio.yaml', remote_load=False)
    for specy in species.values():
        update(specy)
    save_species('/home/francois/species2.yaml', species)


def load_one():
    data = {'inpn': 69627}
    specy = Specy.from_dict(data, remote_load=True)
    save_species('/tmp/species.yaml', {specy.id: specy})


if __name__ == '__main__':
    update_all()
