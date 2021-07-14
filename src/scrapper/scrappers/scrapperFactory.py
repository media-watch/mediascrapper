import json
import os
import src
from src.scrapper.scrappers.webSiteScrappers import (lapresseScrapper, realitiesScrapper, leadersScrapper)

class ScrapperFactory:
    """
    factory class to create scrappers for each of the websites
    """
    
    _site_scrappers = dict()
    
    def __init__(self):
        self._site_scrappers = dict()
        self.setupScrappers()
    
    def setupScrappers(self):
        self._site_scrappers = {
            "realites":realitiesScrapper.RealitiesScrapper(),
            "lapresse":lapresseScrapper.LapresseScrapper(),
            "leaders": leadersScrapper.LeadersScrapper()
        }
            
    def getInstances(self, site):
        return self._site_scrappers[site]
    