from src.scrapper.scrappers.scrapperFactory import ScrapperFactory
from src.scrapper.models.article import Article
from src.db.dbController import DbController
import urllib.request
import logging as lg

_logger = lg.getLogger(__name__)

class DataLoader:

    def __init__(self, site):
        self._site = site["website"]
        self._url = site["url"]
        self._scrapper = ScrapperFactory().getInstances(self._site)
        self._db = DbController(self._site)
                

    def start(self):
        _logger.info("Loader of {} is started".format(self._site))
        self.load_data()

    def load_data(self):
        new_article = Article(self._site)
        with urllib.request.urlopen(self._url) as response:
            html = response.read()
            attrs = self._scrapper.scrap(html)
            new_article.add_attributes(attrs)
            new_article.persist(self._db)