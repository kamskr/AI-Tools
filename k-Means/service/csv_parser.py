import csv
import numpy as np


class CsvParser:
    def __init__(self, training_set_file):
        self.training_set_file = training_set_file

    def parse_training_set(self):
        training_set = []
        with open(self.training_set_file, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                vector = []
                for v in row:
                    try:
                        vector.append(float(v))
                    except ValueError:
                        name = v
                training_set.append(vector)

        return self.normalize_training_set(training_set)

    def normalize_training_set(self, training_set):
        normalized_training_set = []
        temp_list = training_set

        transposed_list = np.transpose(temp_list)

        for vector in temp_list:
            j = 0
            new_vector = []
            for value in vector:
                new_vector.append((value - min(transposed_list[j]))/(max(transposed_list[j]) - min(transposed_list[j])))
                j += 1

            normalized_training_set.append(new_vector)

        return normalized_training_set