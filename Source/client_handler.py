from json import *

class client_hander:
    def __init__(self, file):
        self.file = file
    
    def get_level(self):
        with open(self.file) as json_file:
            temp = load(json_file)
            json_file.close()
            return temp