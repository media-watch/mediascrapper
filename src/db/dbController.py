import os
import json
import src

class DbController:
    
    _db = None
         
    def __init__(self, website):
        self._website = website
        base = os.environ['VIRTUAL_ENV'] if os.environ['VIRTUAL_ENV'] else os.path.dirname(os.path.abspath(src.__file__))
        self._filename = os.path.join(
            os.path.dirname(base),
            "src/db/data/",
            self._website + ".json"
        )
        self.create_if_not_exist()
        
    def create_if_not_exist(self):
        # Create the file if it does not exist
        if not os.path.exists(self._filename):
            with open(self._filename, 'w') as f:
                f.write("[]")
                f.close()
            
    def get_all(self):
        with open(self._filename, "r") as file:
            data = json.load(file)
            return data

    def write_to_json(self, data):
        with open(self._filename, "w") as file:
            json.dump(data, file)
    
    def add_to_json(self, article):
        data = self.get_all()
        data.append(article)
        self.write_to_json(data)
    
    @staticmethod
    def get_all_by_website(website):
        base = os.environ['VIRTUAL_ENV'] if os.environ['VIRTUAL_ENV'] else os.path.dirname(os.path.abspath(src.__file__))
        _filename = os.path.join(
            os.path.dirname(base),
            "src/db/data/",
            website + ".json"
        )
        with open(_filename, "r") as file:
            data = json.load(file)
            return json.dumps(data)
