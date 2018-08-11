from collections import namedtuple

import requests


Manga = namedtuple('Manga', ['url', 'title', 'is_complete'])

class GenericWorker:
    session = requests.session()

    def get_response(self, method, url, **kwargs):
        response = self.session.request(method, url, **kwargs)
        response.raise_for_status()
        return response

    @staticmethod
    def manga_factory(url, title, is_complete):
        manga = Manga(url, title, is_complete)
        return manga