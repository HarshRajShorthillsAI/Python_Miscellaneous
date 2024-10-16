import json
import csv

class ExamResult:
    def __init__(self):
        self.data = None

    
    def connect(self, data_file):
        with open(data_file) as json_file:
            self.data = json.load(json_file)

    def get_div1(self, total):
        return int(total) >= 104