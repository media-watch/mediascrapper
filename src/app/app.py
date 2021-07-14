from flask import Flask
from src.db.dbController import DbController

class AppHelper:
    """
    a singleton app flask class helper contains the dynamic attributes
    """
    _instance = None
    app = Flask(__name__)
    _db = DbController
         
    def __init__(self):
        raise RuntimeError('Call getInstance() instead')
    
    @classmethod
    def getInstance(cls):
        if not cls._instance:
            cls._instance = cls.__new__(cls)
        return cls._instance
    
    def get_app(self): return self.app
    
    def get_db(self): return self._db
    
    def set_sites(self, sites): self._sites = sites
    
    def get_sites(self): return self._sites


class App:
    """
    main flask server class
    contains routes
    """
    app = AppHelper.getInstance().get_app()
    
    def __init__(self, sites):
        AppHelper.getInstance().set_sites(sites)
        
    @staticmethod
    @app.route('/websites/<website>', methods=['POST'])
    def get_by_site(website):
        if website in AppHelper.getInstance().get_sites():
            return AppHelper.getInstance().get_db().get_all_by_website(website)
        else:
            return {}
    
    def start(self):
        self.app.run(host='0.0.0.0', port=5000, debug=True)
    

def main():
    app = App(["leaders", "realites", "lapresse"])
    app.start()

if __name__ == '__main__':
    main()
    