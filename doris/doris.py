""" Class definitions """
from typing import List, Tuple, Dict
import logging
import requests
import yaml
from bs4 import BeautifulSoup


def name(taxon: Dict) -> str:
    """
    Return the common name for a taxon
    @param taxon: the taxon, as a dict
    @return: the name
    """
    _name = None
    if 'vernacular' in taxon['names']:
        if 'fr' in taxon['names']['vernacular']:
            _name = taxon['names']['vernacular']['fr']
        elif 'en' in taxon['names']['vernacular']:
            _name = taxon['names']['vernacular']['en']

    if _name is None:
        _name = taxon['names']['binomial']

    if isinstance(_name, str):
        return _name
    else:
        return ', '.join(_name)


# pylint: disable=too-many-instance-attributes
class Specy:
    """ Represents a specy """
    # pylint: disable=too-many-arguments
    def __init__(self, specy_id, names, link, image, thumbnail,
                 taxonomy=None, photos=None, tags=None):
        """
        the full taxonomy, ex 
            dpomain Biota
            kingdom Animaux
            phylum Annélides, Vers annelés
            class Vers annelés marins, Polychètes
            order Sabellida
            family calcareous tubeworms
            genus Serpula
        """
        self.__name = None
        # pylint: disable=invalid-name
        self.id = specy_id
        self.names = names
        self.link = link
        self.image = image
        self.thumbnail = thumbnail
        if taxonomy is None:
            taxonomy = []
        self.taxonomy = taxonomy
        self.photos = photos
        if tags is None:
            tags = []
        self.tags = tags
        logging.warning('Loaded %s (%s)', specy_id, self.name)

    @property
    def name(self):
        """ Display the specie's name """
        if self.__name:
            return self.__name
        return name(self.__dict__)

    @name.setter
    def name(self, p_name):
        self.__name = p_name

    def __str__(self):
        """ String """
        return self.names['scientific']

    def add_link(self, source, ref):
        """ Manually add a link """
        if source == 'doris':
            self.link['doris'] = f'http://doris.ffessm.fr/ref/specie/{ref}'

    def add_photos(self, src, url=None):
        if src == 'doris':
            resp = requests.get(self.link['doris'])
            soup = BeautifulSoup(resp.text, "html.parser")

            for div in soup.find_all("div", class_="imageInfoShell"):
                try:
                    img = div.img['src']
                    if img.startswith('/'):
                        img = f'http://doris.ffessm.fr{img}'
                    self.photos.append({'url': img, 'src': 'doris'})
                except:
                    pass

            if len([photo for photo in self.photos if photo['src'] == 'doris']) == 0:
                logging.warning('No picture found for %s', self.name)
            else:
                if self.thumbnail is None:
                    self.thumbnail = self.photos[0]['url']
                if self.image is None:
                    self.image = self.photos[0]['url']
        else:
            self.photos.append({'url': url, 'src': src})

    @classmethod
    def from_inpn(cls, ref):
        """ Load from inpn api using their ID """
        url = f'https://taxref.mnhn.fr/api/taxa/{ref}'
        resp = requests.get(url)
        resp.raise_for_status()
        data = resp.json()
        link = {
            'inpn_api': url,
            'inpn': data['_links']['inpnWebpage']['href']
        }

        inpn_external_urls = data['_links']['externalIds']['href']
        resp = requests.get(inpn_external_urls)
        resp.raise_for_status()
        link_data = resp.json()
        for external in link_data['_embedded']['externalDb']:
            if external['externalDbName'] == 'DORIS':
                link['doris'] = external['url']

        inpn_media_urls = data['_links']['media']['href']
        resp = requests.get(inpn_media_urls)
        resp.raise_for_status()
        media_data = resp.json()
        image = None
        thumbnail = None
        photos = []
        for media in media_data['_embedded']['media']:
            if 'image' not in media['mimeType']:
                continue

            if image is None:
                image = media['_links']['file']['href']

            if thumbnail is None:
                thumbnail = media['_links']['thumbnailFile']['href']

            photos.append({'url': media['_links']['file']['href'], 'src': 'inpn'})

        taxonomy = [
            ['domain', data['rankName']],
            ['kingdom', data['kingdomName']],
            ['phylum', data['phylumName']],
            ['class', data['className']],
            ['order', data['orderName']],
            ['family', data['familyName']],
            ['genus', data['genusName']]
        ]

        names = {
            'binomial': data["scientificName"],
            'scientific': data["referenceName"],
            'scientificHtml': data["referenceNameHtml"],
            'vernacular': {
                'fr': data["frenchVernacularName"],
                'en': data["englishVernacularName"]
            }
        }

        return cls(specy_id=ref,
                   names=names, link=link,
                   image=image,
                   thumbnail=thumbnail,
                   taxonomy=taxonomy,
                   photos=photos)

    # pylint: disable=unused-argument
    @classmethod
    def from_name(cls, name):
        """ Search the specie's name on inpn and load """
        url = 'https://inpn.mnhn.fr/inpn-web-services/especes/jdd/listEspece'
        url = f'{url}?idJdd=250&start=0&length=10&search%5Bvalue%5D={name}'
        resp = requests.get(url)
        resp.raise_for_status()
        data = resp.json()['data']
        assert len(data) == 1

        ref = data[0]['CD_REF']
        return cls.from_inpn(ref)

    @classmethod
    def from_dict(cls, data, remote_load=False):
        """
        Load specie according to a dict defition.
        If the dict has:
            - a `specy` key, then use `from_name()`
            - no `specy` key, then use `from_inpn()`
            - a `name` key, then override the default name
            - a `doris` key, then add a link to that doris page
        """
        if remote_load:
            if 'specy' in data and data['specy']:
                specy = Specy.from_name(data['specy'])
            else:
                specy = Specy.from_inpn(data['inpn'])

            if 'doris' in data and data['doris']:
                specy.add_link('doris', data['doris'])

            # Load additional photos from the doris website
            if 'doris' in specy.link:
                specy.add_photos('doris')
        else:
            if 'taxonomy' in data:
                taxonomy = data['taxonomy']
            else:
                taxonomy = None
            if 'photos' in data:
                photos = data['photos']
            else:
                photos = None
            if 'tags' in data:
                tags = data['tags']
            else:
                tags = None
            specy = cls(specy_id=data['id'],
                        names=data['names'],
                        link=data['link'],
                        image=data['image'],
                        thumbnail=data['thumbnail'],
                        taxonomy=taxonomy,
                        photos=photos,
                        tags=tags)

        if 'name' in data and data['name']:
            specy.name = data['name']

        return specy

    def dump(self):
        _dict = self.__dict__.copy()
        if _dict['_Specy__name'] is not None:
            _dict['name'] = _dict['_Specy__name']
        del(_dict['_Specy__name'])
        return _dict


def load_species(filename: str, remote_load=True) -> (Dict[int, Specy], List):
    """ Load all species in the configuration file """
    species = {}
    tags = []
    with open(filename, 'r') as stream:
        data = yaml.safe_load(stream)
        for specy_dict in data['species']:
            specy = Specy.from_dict(specy_dict, remote_load=remote_load)
            species[specy.id] = specy
    return species, data['tags']


def save_species(filename: str, species: dict, tags: list) -> None:
    """ Save all species """
    with open(filename, "w") as myfile:
        myfile.write(yaml.safe_dump({
            'tags': tags,
            'species': [specy.dump() for specy in species.values()]
        }))
