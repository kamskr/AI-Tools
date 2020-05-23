import csv 
from model.vector import Vector


class CsvParser:
    def __init__(self, training_set_file):
        self.training_set_file = training_set_file

    def parse_training_set(self):
        training_set = []
        with open(self.training_set_file, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                vector = []
                name = ""
                for v in row:
                    try:
                        vector.append(float(v))
                    except ValueError:
                        name = v
                training_set.append(Vector(name, vector))
        return training_set


