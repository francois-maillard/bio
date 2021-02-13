""" Class definitions """
from typing import Dict
import logging
import requests
import yaml


# pylint: disable=too-many-instance-attributes
class Specy:
    """ Represents a specy """
    # pylint: disable=too-many-arguments
    def __init__(self, specy_id, names, link, image, thumbnail, photos=None):
        self.__name = None
        # pylint: disable=invalid-name
        self.id = specy_id
        self.names = names
        self.link = link
        self.image = image
        self.thumbnail = thumbnail
        self.photos = photos
        logging.warning('Loaded %s (%s)', specy_id, self.name)

    @property
    def name(self):
        """ Display the specie's name """
        if self.__name is not None:
            return self.__name

        if 'vernacular' in self.names:
            if 'fr' in self.names['vernacular']:
                return self.names['vernacular']['fr']
            if 'en' in self.names['vernacular']:
                return self.names['vernacular']['en']

        return self.names['binomial']

    @name.setter
    def name(self, p_name):
        self.__name = p_name

    def __str__(self):
        """ String """
        return self.names['scientific']

    def addlink(self, source, ref):
        """ Manually add a link """
        if source == 'doris':
            self.link['doris'] = f'http://doris.ffessm.fr/ref/specie/{ref}'

    @classmethod
    def from_inpn(cls, ref):
        """ Load from inpn api using their ID """
        url = f'https://odata-inpn.mnhn.fr/taxons/{ref}?embed=PHOTOS'
        resp = requests.get(url)
        resp.raise_for_status()
        data = resp.json()
        link = {
            'inpn_api': url,
            'inpn': f'https://inpn.mnhn.fr/espece/cd_nom/{ref}'
        }

        link_url = f'https://taxref.mnhn.fr/api/taxa/{ref}/externalIds'

        resp = requests.get(link_url)
        resp.raise_for_status()
        link_data = resp.json()
        for external in link_data['_embedded']['externalDb']:
            if external['externalDbName'] == 'DORIS':
                link['doris'] = external['url']

        image = None
        if 'image' in data['_links']:
            image = data['_links']['image']['href']

        thumbnail = None
        if 'thumbnail' in data['_links']:
            thumbnail = data['_links']['thumbnail']['href']

        return cls(specy_id=ref,
                   names=data['names'], link=link,
                   image=image,
                   thumbnail=thumbnail,
                   photos=[photo['_links']['image']['href'] for photo in
                           data['_embedded']['photos']])

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
    def from_dict(cls, data):
        """
        Load specie according to a dict defition.
        If the dict has:
            - a `specy` key, then use `from_name()`
            - no `specy` key, then use `from_inpn()`
            - a `name` key, then override the default name
            - a `doris` key, then add a link to that doris page
        """
        if 'specy' in data and data['specy']:
            specy = Specy.from_name(data['specy'])
        else:
            specy = Specy.from_inpn(data['inpn'])

        if 'name' in data and data['name']:
            specy.name = data['name']
        if 'doris' in data and data['doris']:
            specy.addlink('doris', data['doris'])
        return specy


def load_species(filename: str) -> Dict[int, Specy]:
    """ Load all species in the configuration file """
    species = {}
    with open(filename, 'r') as stream:
        for data in yaml.safe_load(stream):
            specy = Specy.from_dict(data)
            species[specy.id] = specy
    return species


def save_specy(filename: str, data: dict) -> None:
    """ Add the specy at the end of the file """
    _data = {}
    for key, value in data.items():
        if value:
            _data[key] = value
    with open(filename, "a") as myfile:
        myfile.write(yaml.safe_dump([_data]))
