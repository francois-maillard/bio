""" Class definitions """
from typing import Dict
import logging
import requests
import yaml
from bs4 import BeautifulSoup


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

    def add_link(self, source, ref):
        """ Manually add a link """
        if source == 'doris':
            self.link['doris'] = f'http://doris.ffessm.fr/ref/specie/{ref}'

    def add_photos(self, src, url=None):
        if src == 'doris':
            resp = requests.get(self.link['doris'])
            soup = BeautifulSoup(resp.text, "html.parser")

            for div in soup.find_all("div", class_="imageInfoShell"):
                if not div.img:
                    continue

                img = div.img['src']
                if img.startswith('/'):
                    img = f'http://doris.ffessm.fr{img}'
                self.photos.append({'url': img, 'src': 'doris'})

            if len([photo for photo in self.photos if photo['src'] == 'doris']) == 0:
                logging.warning('No picture found for %s', self.name)
        else:
            self.photos.append({'url': url, 'src': src})

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
                   photos=[{'url': photo['_links']['image']['href'], 'src': 'inpn'}
                           for photo in data['_embedded']['photos']])

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
        else:
            if 'photos' in data:
                photos = data['photos']
            else:
                photos = None
            specy = cls(specy_id=data['id'],
                        names=data['names'],
                        link=data['link'],
                        image=data['image'],
                        thumbnail=data['thumbnail'],
                        photos=photos)

        if 'name' in data and data['name']:
            specy.name = data['name']

        if 'doris' in data and data['doris']:
            specy.add_link('doris', data['doris'])
            specy.add_photos('doris')

        return specy

    def dump(self):
        _dict = self.__dict__.copy()
        if _dict['_Specy__name'] is not None:
            _dict['name'] = _dict['_Specy__name']
        del(_dict['_Specy__name'])
        return _dict


def load_species(filename: str, remote_load=True) -> Dict[int, Specy]:
    """ Load all species in the configuration file """
    species = {}
    with open(filename, 'r') as stream:
        for data in yaml.safe_load(stream):
            specy = Specy.from_dict(data, remote_load=remote_load)
            species[specy.id] = specy
    return species


def save_species(filename: str, data: dict) -> None:
    """ Save all species """
    with open(filename, "w") as myfile:
        for specy in data.values():
            myfile.write(yaml.safe_dump([specy.dump()]))
