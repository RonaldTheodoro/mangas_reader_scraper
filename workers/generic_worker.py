import logging
from collections import namedtuple

import requests

logging.basicConfig(
    level=logging.DEBUG,
    format=' %(asctime)s - %(levelname)s - %(message)s'
)

Manga = namedtuple('Manga', ['url', 'title', 'is_complete'])

class GenericWorker:
    session = requests.session()

    def get_response(self, method, url, **kwargs):
        try:
            response = self.session.request(method, url, **kwargs)
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            logging.critical('An error happened during the request')
        else:
            return response

        return None

    @staticmethod
    def manga_factory(url, title, is_complete):
        manga = Manga(url, title, is_complete)
        return manga

    def get_manga_list(self, save=False):

        response = self.get_catalog()

        mangas = self.parse_catalog(response)

        if save:
            mangas = self.save_mangas(mangas)

        return mangas

    def get_catalog(self):
        raise NotImplementedError('This method must be implemented')

    def parse_catalog(self, response):
        raise NotImplementedError('This method must be implemented')

    def save_mangas(self, mangas):
        raise NotImplementedError('This method must be implemented')
