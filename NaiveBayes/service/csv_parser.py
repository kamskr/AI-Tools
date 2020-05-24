import csv


class CsvParser:
    def __init__(self, training_set_file, test_set_file):
        self.training_set_file = training_set_file
        self.test_set_file = test_set_file

    def parse_training_set(self):
        training_set = self.parse_set(self.training_set_file)
        return training_set

    def parse_test_set(self):
        test_set = self.parse_set(self.test_set_file)
        return test_set

    @staticmethod
    def parse_set(data_file):
        parsed_set = []
        with open(data_file, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                row_dict = dict()
                for column in range(len(row)):
                    row_dict[column] = row[column]
                parsed_set.append(row_dict)
        return parsed_set

