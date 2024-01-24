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
            ['domain', 'Espèce'],
            ['kingdom', 'Animalia'],
            ['phylum', 'Chordata'],
            ['class', 'Actinopterygii'],
            ['order', 'Anguilliformes'],
            ['family', 'Congridae'],
            ['genus', 'Conger'],
        ],
        'image': 'https://taxref.mnhn.fr/api/media/download/inpn/128704',
        'thumbnail': 'https://taxref.mnhn.fr/api/media/download/thumbnail/128704',
        'photos': [
            {'src': 'inpn', 'url': 'https://taxref.mnhn.fr/api/media/download/inpn/128704'},
            {'src': 'inpn', 'url': 'https://odata-inpn.mnhn.fr/photos/images/3/266443.jpg'}
        ],
        'link': {
            'inpn_api': 'https://taxref.mnhn.fr/api/taxa/66921',
            'inpn': 'https://inpn.mnhn.fr/espece/cd_nom/66921',
            'doris': 'http://doris.ffessm.fr/ref/specie/610'
        }
    },
    547264: {
        'id': 547264,
        'name': 'Antiopelle',
        'names': {
            'binomial': 'Antiopella cristata',
            'scientific': 'Antiopella cristata (Delle Chiaje, 1841)',
            'scientificHtml': '<i>Antiopella cristata</i> (Delle Chiaje, 1841)',
            'vernacular': {
                'fr': None,
                'en': None
            }
        },
        'link': {
            'inpn_api': 'https://taxref.mnhn.fr/api/taxa/547264',
            'inpn': 'https://inpn.mnhn.fr/espece/cd_nom/547264',
            'doris': 'http://doris.ffessm.fr/ref/specie/335'
        },
        'image': 'https://taxref.mnhn.fr/api/media/download/inpn/219858',
        'thumbnail': 'https://taxref.mnhn.fr/api/media/download/thumbnail/219858',
        'taxonomy': [
            ['domain', 'Espèce'],
            ['kingdom', 'Animalia'],
            ['phylum', 'Mollusca'],
            ['class', 'Gastropoda'],
            ['order', 'Nudibranchia'],
            ['family', 'Janolidae'],
            ['genus', 'Antiopella']
        ],
        'tags': ['foo'],
        'photos': [
            {'url': 'https://taxref.mnhn.fr/api/media/download/inpn/219858', 'src': 'inpn'},
            {'url': 'https://taxref.mnhn.fr/api/media/download/inpn/219857', 'src': 'inpn'},
            {'url': 'https://taxref.mnhn.fr/api/media/download/inpn/243236', 'src': 'inpn'},
            {'url': 'https://taxref.mnhn.fr/api/media/download/inpn/243240', 'src': 'inpn'},
            {'url': 'https://taxref.mnhn.fr/api/media/download/inpn/243241', 'src': 'inpn'},
            {'url': 'https://doriscdn.ffessm.fr/var/doris/storage/images/images/ramifications-des-organes-digestifs-17863/155913-1-fre-FR/janolus_cristatus-aps01_image1200.jpg', 'src': 'doris'},
            {'url': 'https://doriscdn.ffessm.fr/var/doris/storage/images/images/janolus_cristatus-vima17/156561-1-fre-FR/janolus_cristatus-vima17_image1200.jpg', 'src': 'doris'},
            {'url': 'https://doriscdn.ffessm.fr/var/doris/storage/images/images/janolus_cristatus-db124/156905-1-fre-FR/janolus_cristatus-db124_image1200.jpg', 'src': 'doris'},
            {'url': 'https://doriscdn.ffessm.fr/var/doris/storage/images/images/janolus_cristatus-gd766/253617-1-fre-FR/janolus_cristatus-gd766_image1200.jpg', 'src': 'doris'},
            {'url': 'https://doriscdn.ffessm.fr/var/doris/storage/images/images/mimetisme-17918/156353-1-fre-FR/janolus_cristatus-aps11_image1200.jpg', 'src': 'doris'},
            {'url': 'https://doriscdn.ffessm.fr/var/doris/storage/images/images/janolus_cristatus-vl4201/156361-1-fre-FR/janolus_cristatus-vl4201_image1200.jpg', 'src': 'doris'},
            {'url': 'https://doriscdn.ffessm.fr/var/doris/storage/images/images/details-dorsaux-22082/189665-1-fre-FR/janolus_cristatus-aps091_image1200.jpg', 'src': 'doris'},
            {'url': 'https://doriscdn.ffessm.fr/var/doris/storage/images/images/janolus_cristatus-frhe80/2481451-1-fre-FR/janolus_cristatus-frhe80_image1200.jpg', 'src': 'doris'},
            {'url': 'https://doriscdn.ffessm.fr/var/doris/storage/images/images/attitude-de-defense-17932/156465-1-fre-FR/janolus_cristatus-161_image1200.jpg', 'src': 'doris'},
            {'url': 'https://doriscdn.ffessm.fr/var/doris/storage/images/images/nourriture-17920/156369-1-fre-FR/janolus_cristatu-vl31_image1200.jpg', 'src': 'doris'},
            {'url': 'https://doriscdn.ffessm.fr/var/doris/storage/images/images/janolus_cristatus-aps10/189673-1-fre-FR/janolus_cristatus-aps10_image1200.jpg', 'src': 'doris'},
            {'url': 'https://doriscdn.ffessm.fr/var/doris/storage/images/images/janolus_cristatus-hesera2016/2481467-1-fre-FR/janolus_cristatus-hesera2016_image1200.jpg', 'src': 'doris'},
            {'url': 'https://doriscdn.ffessm.fr/var/doris/storage/images/images/dans-l-halimede-25748/218993-1-fre-FR/janolus_cristatus-cgras9101_image1200.jpg', 'src': 'doris'},
            {'url': 'https://doriscdn.ffessm.fr/var/doris/storage/images/images/copepode-parasite-33081/277657-1-fre-FR/janolus_cristatus_mf_2221_image1200.jpg', 'src': 'doris'},
            {'url': 'https://doriscdn.ffessm.fr/var/doris/storage/images/images/copepodes-parasites-2-39711/330697-1-fre-FR/doridicola_sp-dead9981_image1200.jpg', 'src': 'doris'},
            {'url': 'https://doriscdn.ffessm.fr/var/doris/storage/images/images/en-mer-du-nord-17931/156457-1-fre-FR/janolus_cristatus-151_image1200.jpg', 'src': 'doris'},
            {'url': 'https://doriscdn.ffessm.fr/var/doris/storage/images/images/trio-en-languedoc-roussillon-24678/210433-1-fre-FR/janolus_cristatus-hr119341_image1200.jpg', 'src': 'doris'},
            {'url': 'https://doriscdn.ffessm.fr/var/doris/storage/images/images/janolus_cristatus-stja201606/2510881-1-fre-FR/janolus_cristatus-stja201606_image1200.jpg', 'src': 'doris'},
            {'url': 'https://doriscdn.ffessm.fr/var/doris/storage/images/images/janolus_cristatus-cg252/210441-1-fre-FR/janolus_cristatus-cg252_image1200.jpg', 'src': 'doris'},
            {'url': 'https://doriscdn.ffessm.fr/var/doris/storage/images/images/duo-italien-24680/210449-1-fre-FR/janolus_cristatus-sj6661_image1200.jpg', 'src': 'doris'}
        ]
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
    print(specy.taxonomy)
    assert specy.taxonomy == SPECIES[CD_REF]['taxonomy']


def test_specy_addlink():
    CD_REF = 547264
    specy = Specy.from_inpn(CD_REF)
    assert 'doris' not in specy.link
    specy.add_link('doris', 335)
    assert specy.link['doris'] == SPECIES[CD_REF]['link']['doris']


def test_specy_name():
    CD_REF = 547264
    specy = Specy.from_inpn(CD_REF)
    assert specy.name == 'Antiopella cristata'
    specy.name = 'Antiopelle'
    assert specy.name == 'Antiopelle'


def test_specy_from_name():
    specy = Specy.from_name('conger')
    assert specy.names['binomial'] == 'Conger conger'


def test_specy_from_dict():
    specy = Specy.from_dict({'specy': 'Conger'}, remote_load=True)
    assert specy.names['binomial'] == 'Conger conger'

    CD_REF = 547264
    specy = Specy.from_dict({'inpn': CD_REF}, remote_load=True)
    assert specy.name == 'Antiopella cristata'
    assert 'doris' not in specy.link

    specy = Specy.from_dict({'inpn': CD_REF, 'name': 'Antiopelle'}, remote_load=True)
    assert specy.name == 'Antiopelle'

    specy = Specy.from_dict({'inpn': CD_REF, 'doris': 335}, remote_load=True)
    assert specy.link['doris'] == 'http://doris.ffessm.fr/ref/specie/335'


def test_specy_dump():
    CD_REF = 547264
    specy = Specy.from_dict({'inpn': CD_REF, 'doris': 335, 'name': 'Antiopelle'}, remote_load=True)
    assert specy.name == 'Antiopelle'
    dump = specy.dump()
    assert dump['name'] == 'Antiopelle'
    assert specy.name == 'Antiopelle'


def test_load_species():
    (species, tags) = load_species(os.path.join(TEST_ROOT, 'species.yaml'))
    assert len(species) == 4
    assert species[66921].names['binomial'] == 'Conger conger'
    assert species[547264].link['doris'] == 'http://doris.ffessm.fr/ref/specie/335'


def test_load_species_local():
    (species, tags) = load_species(os.path.join(TEST_ROOT, 'species-all.yaml'), remote_load=False)
    assert len(species) == 2
    assert species[547264].dump() == SPECIES[547264]

    assert len(tags) == 2
    assert tags[0] == 'foo'

    assert len(species[66921].tags) == 0
    assert species[547264].tags == ['foo']

    filtered = {specy.id: specy for specy in species.values() if set(specy.tags) & set(tags)}
    assert len(filtered) == 1
    assert filtered[547264].dump() == SPECIES[547264]
