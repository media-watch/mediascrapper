import logging as lg

_logger = lg.getLogger(__name__)

class Article:
    
    """
    class article model
    """    
    def __init__(self, site):
        # self._required = {"title","article", "site", "date", "topics", "word_cloud"} @TODO
        self._required = {"title","article", "site", "date"}
        self._required_attrs_exist = False
        self._attributes = {"site":site}
        
    def check_required(self):
        self._required_attrs_exist = self._required.issubset(self._attributes)
    
    def add_attributes(self, attrs):
        self._attributes.update(attrs)
        if not self._required_attrs_exist: self.check_required()
        
    def persist(self, db):
        if self._required_attrs_exist: 
            _logger.info("Aricle {} of {} is loaded in DB".format(self._attributes["title"],self._attributes["site"]))
            db.add_to_json(self._attributes)