__author__ = 'root'

import json


class NotebookParser:

    def parse(self, path):
        json_data = open(path)
        data = json.load(json_data)
        json_data.close()
        return data