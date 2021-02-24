import os
from doris.doris import Specy, load_species

TEST_ROOT = os.path.dirname(os.path.abspath(__file__))

SPECIES = {
    66921: {
        'id': 66921,
        'name': 'Congre',
        'names': {
            'binomial': 'Conger conger',
            'vernacular': {
                'fr': 'Congre d’Europe'
            }
        },
        'image': 'https://odata-inpn.mnhn.fr/photos/images/2/266442.jpg',
        'thumbnail': 'https://odata-inpn.mnhn.fr/photos/thumbnails/2/266442.jpg',
        'photos': [
            'https://odata-inpn.mnhn.fr/photos/images/2/266442.jpg',
            'https://odata-inpn.mnhn.fr/photos/images/3/266443.jpg'
        ],
        'link': {
            'inpn_api': 'https://odata-inpn.mnhn.fr/taxons/66921?embed=PHOTOS',
            'inpn': 'https://inpn.mnhn.fr/espece/cd_nom/66921',
            'doris': 'http://doris.ffessm.fr/ref/specie/610'
        }
    },
    63607: {
        'id': 63607,
        'image': 'https://odata-inpn.mnhn.fr/photos/images/1/243291.jpg',
        'link': {
          'doris': 'http://doris.ffessm.fr/ref/specie/169',
          'inpn': 'https://inpn.mnhn.fr/espece/cd_nom/63607',
          'inpn_api': 'https://odata-inpn.mnhn.fr/taxons/63607?embed=PHOTOS'
        },
        'name': 'Doris Dalmatienne',
        'names': {
          'binomial': 'Peltodoris atromaculata',
          'scientific': 'Peltodoris atromaculata Bergh, 1880',
          'scientificHtml': '<i>Peltodoris atromaculata</i> Bergh, 1880',
          'vernacular': {}
        },
        'photos': [
            'https://odata-inpn.mnhn.fr/photos/images/9/243289.jpg',
            'https://odata-inpn.mnhn.fr/photos/images/1/243291.jpg',
            'https://odata-inpn.mnhn.fr/photos/images/0/243290.jpg',
            'https://odata-inpn.mnhn.fr/photos/images/5/120665.jpg',
            'https://odata-inpn.mnhn.fr/photos/images/5/143345.jpg'
        ],
        'thumbnail': 'https://odata-inpn.mnhn.fr/photos/thumbnails/1/243291.jpg'
    }
}

def test_specy_from_inpn():
    CD_REF = 66921
    specy = Specy.from_inpn(CD_REF)
    assert specy.names['binomial'] == SPECIES[CD_REF]['names']['binomial']
    assert specy.names['vernacular']['fr'] == SPECIES[CD_REF]['names']['vernacular']['fr']
    assert specy.image == SPECIES[CD_REF]['image']
    assert specy.thumbnail == SPECIES[CD_REF]['thumbnail']
    assert specy.photos[0] in SPECIES[CD_REF]['photos']
    assert specy.link['inpn_api'] == SPECIES[CD_REF]['link']['inpn_api']
    assert specy.link['inpn'] == SPECIES[CD_REF]['link']['inpn']
    assert specy.link['doris'] == SPECIES[CD_REF]['link']['doris']


def test_specy_addlink():
    CD_REF = 63607
    specy = Specy.from_inpn(CD_REF)
    assert 'doris' not in specy.link
    specy.addlink('doris', 169)
    assert specy.link['doris'] == SPECIES[CD_REF]['link']['doris']


def test_specy_name():
    CD_REF = 63607
    specy = Specy.from_inpn(CD_REF)
    assert specy.name == 'Peltodoris atromaculata'
    specy.name = 'Doris dalmatienne'
    assert specy.name == 'Doris dalmatienne'


def test_specy_from_name():
    specy = Specy.from_name('conger')
    assert specy.names['binomial'] == 'Conger conger'


def test_specy_from_dict():
    specy = Specy.from_dict({'specy': 'Conger'}, remote_load=True)
    assert specy.names['binomial'] == 'Conger conger'

    CD_REF = 63607
    specy = Specy.from_dict({'inpn': CD_REF}, remote_load=True)
    assert specy.name == 'Peltodoris atromaculata'
    assert 'doris' not in specy.link

    specy = Specy.from_dict({'inpn': CD_REF, 'name': 'Doris dalmatienne'}, remote_load=True)
    assert specy.name == 'Doris dalmatienne'

    specy = Specy.from_dict({'inpn': CD_REF, 'doris': 169}, remote_load=True)
    assert specy.link['doris'] == 'http://doris.ffessm.fr/ref/specie/169'


def test_specy_dump():
    CD_REF = 63607
    specy = Specy.from_dict({'inpn': CD_REF, 'doris': 169, 'name': 'Doris dalmatienne'}, remote_load=True)
    assert specy.name == 'Doris dalmatienne'
    dump = specy.dump()
    assert dump['name'] == 'Doris dalmatienne'
    assert specy.name == 'Doris dalmatienne'


def test_load_species():
    species = load_species(os.path.join(TEST_ROOT, 'species.yaml'))
    assert len(species) == 4
    assert species[66921].names['binomial'] == 'Conger conger'
    assert species[63607].link['doris'] == 'http://doris.ffessm.fr/ref/specie/169'


def test_load_species_local():
    species = load_species(os.path.join(TEST_ROOT, 'species-all.yaml'), remote_load=False)
    assert len(species) == 1
    assert species[63607].dump() == SPECIES[63607]
