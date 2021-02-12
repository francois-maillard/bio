import os
from doris.doris import Specy, load_species

TEST_ROOT = os.path.dirname(os.path.abspath(__file__))


def test_specy_from_inpn():
    CD_REF = 66921
    specy = Specy.from_inpn(CD_REF)
    assert specy.names['binomial'] == 'Conger conger'
    assert specy.names['vernacular']['fr'] == 'Congre d’Europe'
    assert specy.image == 'https://odata-inpn.mnhn.fr/photos/images/2/266442.jpg'
    assert specy.photos[0] == 'https://odata-inpn.mnhn.fr/photos/images/2/266442.jpg'
    assert specy.link['inpn_api'] == 'https://odata-inpn.mnhn.fr/taxons/66921?embed=PHOTOS'
    assert specy.link['inpn'] == 'https://inpn.mnhn.fr/espece/cd_nom/66921'
    assert specy.link['doris'] == 'http://doris.ffessm.fr/ref/specie/610'


def test_specy_addlink():
    CD_REF = 63607
    specy = Specy.from_inpn(CD_REF)
    assert 'doris' not in specy.link
    specy.addlink('doris', 169)
    assert specy.link['doris'] == 'http://doris.ffessm.fr/ref/specie/169'


def test_specy_name():
    CD_REF = 63607
    specy = Specy.from_inpn(CD_REF)
    assert specy.name == 'Peltodoris atromaculata'
    specy.name = 'Doris dalmatienne'
    assert specy.name == 'Doris dalmatienne'


def test_specy_from_name():
    specy = Specy.from_name('conger')
    assert specy.names['binomial'] == 'Conger conger'


def test_load_species():
    species = load_species(os.path.join(TEST_ROOT, 'species.yaml'))
    assert len(species) == 5
    assert species[0].names['binomial'] == 'Conger conger'
    assert species[2].link['doris'] == 'http://doris.ffessm.fr/ref/specie/169'