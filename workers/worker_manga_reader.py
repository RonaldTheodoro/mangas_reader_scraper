import regex
import requests
from lxml import html

from workers.generic_worker import GenericWorker


class WorkerMangaReader(GenericWorker):
    url_base = 'https://www.mangareader.net'
    url_manga_list = url_base + '/alphabetical'

    def get_manga_list(self):
        response = self.get_response('GET', self.url_manga_list)
        
        root = html.fromstring(response.text)

        mangas = root.xpath('//ul[@class="series_alpha"]/li')

        mangas = [self.create_manga_dict(manga) for manga in mangas]

        print(len(mangas))

        print(mangas[:5])

    def create_manga_dict(self, manga_element):
        url = manga_element.xpath('./a/@href').pop()
        title = manga_element.text_content()

        title, is_complete = self.format_title(title)

        manga = self.manga_factory(url, title, is_complete)
        return manga

    def format_title(self, title):
        completed = regex.compile(r'\[Completed\]', flags=regex.V1)
        is_complete = completed.search(title)

        if is_complete is not None:
            title = completed.sub(r'', title)
            is_complete = True
        else:
            is_complete = False
        return title, is_complete
