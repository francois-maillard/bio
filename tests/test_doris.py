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
        'taxonomy': [
            ['domain', 'Biota'],
            ['kingdom', 'Animaux'],
            ['phylum', 'Chordés'],
            ['class', 'Actinopterygiens, Poissons actinoptérygiens'],
            ['order', 'Anguilles'],
            ['family', 'conger eels'],
            ['sub_family', 'Congrinae'],
            ['genus', 'Conger']
        ],
        'image': 'https://odata-inpn.mnhn.fr/photos/images/2/266442.jpg',
        'thumbnail': 'https://odata-inpn.mnhn.fr/photos/thumbnails/2/266442.jpg',
        'photos': [
            {'src': 'inpn', 'url': 'https://odata-inpn.mnhn.fr/photos/images/2/266442.jpg'},
            {'src': 'inpn', 'url': 'https://odata-inpn.mnhn.fr/photos/images/3/266443.jpg'}
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
        'taxonomy': [
          ['domain', 'Biota'],
          ['kingdom', 'Animaux'],
          ['phylum', 'Mollusques'],
          ['class', "Gast\xE9ropodes"],
          ['order', 'nudibranchs'],
          ['family', 'Discodorididae'],
          ['genus', 'Peltodoris']
        ],
        'name': 'Doris Dalmatienne',
        'names': {
          'binomial': 'Peltodoris atromaculata',
          'scientific': 'Peltodoris atromaculata Bergh, 1880',
          'scientificHtml': '<i>Peltodoris atromaculata</i> Bergh, 1880',
          'vernacular': {}
        },
        'photos': [
            {'src': 'inpn', 'url': 'https://odata-inpn.mnhn.fr/photos/images/9/243289.jpg'},
            {'src': 'inpn', 'url': 'https://odata-inpn.mnhn.fr/photos/images/0/243290.jpg'},
            {'src': 'inpn', 'url': 'https://odata-inpn.mnhn.fr/photos/images/1/243291.jpg'},
            {'src': 'inpn', 'url': 'https://odata-inpn.mnhn.fr/photos/images/5/120665.jpg'},
            {'src': 'inpn', 'url': 'https://odata-inpn.mnhn.fr/photos/images/5/143345.jpg'},
            {'src': 'doris', 'url': 'http://doris.ffessm.fr/var/doris/storage/images/images/detail-du-panache-branchial-16997/148985-1-fre-FR/peltodoris_atromaculata-61_image1200.jpg'},
            {'src': 'doris', 'url': 'http://doris.ffessm.fr/var/doris/storage/images/images/rhinophores-lamelles-16965/148729-1-fre-FR/peltodoris_atromaculata-41_image1200.jpg'},
            {'src': 'doris', 'url': 'http://doris.ffessm.fr/var/doris/storage/images/media/images/peltodoris_atromaculata-cc1/4652421-4-fre-FR/peltodoris_atromaculata-cc1_image1200.jpg'},
            {'src': 'doris', 'url': 'http://doris.ffessm.fr/var/doris/storage/images/media/images/peltodoris_atromaculata-ms1/2218218-5-fre-FR/peltodoris_atromaculata-ms1_image1200.jpg'},
            {'src': 'doris', 'url': 'http://doris.ffessm.fr/var/doris/storage/images/images/aspect-granuleux-du-manteau-17546/153377-1-fre-FR/peltodoris_atromaculata-91_image1200.jpg'},
            {'src': 'doris', 'url': 'http://doris.ffessm.fr/var/doris/storage/images/images/excretion-de-mucus-17929/156441-1-fre-FR/peltodoris_atromaculata-191_image1200.jpg'},
            {'src': 'doris', 'url': 'http://doris.ffessm.fr/var/doris/storage/images/images/doris-dalmatiens-sur-petrosia-ficiformis-16964/148721-1-fre-FR/peltodoris_atromaculata-31_image1200.jpg'},
            {'src': 'doris', 'url': 'http://doris.ffessm.fr/var/doris/storage/images/images/en-dalmatie-17945/156569-1-fre-FR/peltodoris_atromaculata-201_image1200.jpg'},
            {'src': 'doris', 'url': 'http://doris.ffessm.fr/var/doris/storage/images/images/peltodoris_atromaculata-1/156449-1-fre-FR/peltodoris_atromaculata-1_image1200.jpg'},
            {'src': 'doris', 'url': 'http://doris.ffessm.fr/var/doris/storage/images/images/peltodoris_atromaculata-vl10/3578918-1-fre-FR/peltodoris_atromaculata-vl10_image1200.jpg'},
            {'src': 'doris', 'url': 'http://doris.ffessm.fr/var/doris/storage/images/images/organe-sexuel-35203/294633-1-fre-FR/peltodoris_atromaculata-aps81_image1200.jpg'},
            {'src': 'doris', 'url': 'http://doris.ffessm.fr/var/doris/storage/images/images/accouplement-16966/148737-1-fre-FR/peltodoris_atromaculata-vl11_image1200.jpg'},
            {'src': 'doris', 'url': 'http://doris.ffessm.fr/var/doris/storage/images/media/images/peltodoris_atromaculata-za1/3730752-3-fre-FR/peltodoris_atromaculata-za1_image1200.jpg'},
            {'src': 'doris', 'url': 'http://doris.ffessm.fr/var/doris/storage/images/images/doris-dalmatien-et-sa-ponte-16962/148705-1-fre-FR/peltodoris_atromaculata-11_image1200.jpg'},
            {'src': 'doris', 'url': 'http://doris.ffessm.fr/var/doris/storage/images/images/juvenile-28766/243137-1-fre-FR/peltodoris_atromaculata-fa21_image1200.jpg'},
            {'src': 'doris', 'url': 'http://doris.ffessm.fr/var/doris/storage/images/images/copepode-parasite-36784/307281-1-fre-FR/peltodoris_atromaculata_7941_vm1_image1200.jpg'},
            {'src': 'doris', 'url': 'http://doris.ffessm.fr/var/doris/storage/images/images/peltodoris_atromaculata_pg11/223817-1-fre-FR/peltodoris_atromaculata_pg11_image1200.jpg'},
            {'src': 'doris', 'url': 'http://doris.ffessm.fr/var/doris/storage/images/images/la-vie-a-l-ombre-37507/313065-1-fre-FR/peltodoris_atromaculata-sg11_image1200.jpg'},
            {'src': 'doris', 'url': 'http://doris.ffessm.fr/var/doris/storage/images/images/structure-en-tipi-des-spicules-16998/148993-1-fre-FR/peltodoris_atromaculata-71_image1200.jpg'},
            {'src': 'doris', 'url': 'http://doris.ffessm.fr/var/doris/storage/images/images/detail-des-spicules-calcaires-16999/149001-1-fre-FR/peltodoris_atromaculata-81_image1200.jpg'},
            {'src': 'doris', 'url': 'http://doris.ffessm.fr/var/doris/storage/images/media/images/peltodoris_atromaculata-mn1/2481687-1-fre-FR/peltodoris_atromaculata-mn1_image1200.jpg'}
        ],
        'thumbnail': 'https://odata-inpn.mnhn.fr/photos/thumbnails/1/243291.jpg'
    }
}

def test_specy_from_inpn():
    CD_REF = 66921
    specy = Specy.from_inpn(CD_REF)
    assert specy.names['binomial'] == SPECIES[CD_REF]['names']['binomial']
    assert specy.names['vernacular']['fr'][0] == SPECIES[CD_REF]['names']['vernacular']['fr']
    assert specy.image == SPECIES[CD_REF]['image']
    assert specy.thumbnail == SPECIES[CD_REF]['thumbnail']
    assert specy.photos[0] in SPECIES[CD_REF]['photos']
    assert specy.link['inpn_api'] == SPECIES[CD_REF]['link']['inpn_api']
    assert specy.link['inpn'] == SPECIES[CD_REF]['link']['inpn']
    assert specy.link['doris'] == SPECIES[CD_REF]['link']['doris']
    print(specy.taxonomy)
    assert specy.taxonomy == SPECIES[CD_REF]['taxonomy']


def test_specy_addlink():
    CD_REF = 63607
    specy = Specy.from_inpn(CD_REF)
    assert 'doris' not in specy.link
    specy.add_link('doris', 169)
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
