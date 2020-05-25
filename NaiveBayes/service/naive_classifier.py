from service.csv_parser import CsvParser
from collections import defaultdict


class NaiveClassifier:
    def __init__(self, parser: CsvParser):
        self.training_set = parser.parse_training_set()
        self.test_set = parser.parse_test_set()
        self.probabilities = dict()
        self.unique_classifier_dict = self.prepare_data()

    def classify(self):
        total_rows = len(self.test_set)
        correct = 0
        for row in self.test_set:
            result, expected_output = self.classify_row(row)
            if result == expected_output:
                correct += 1

        print("total rows: ", total_rows, "correct:", correct)

    def classify_row(self, row: dict):
        probability_of_classification = dict()
        expected_output = row[len(row) - 1]
        for classifier in self.probabilities:
            total_probability = self.probabilities.get(classifier)
            for i in range(len(row) - 1):
                counter = 0
                total = 0
                for row_in_unique_classifier in self.unique_classifier_dict[classifier]:
                    if row[i] == row_in_unique_classifier[i]:
                        counter += 1
                        total += 1
                    else:
                        total += 1
                probability = counter / total
                if probability == 0:
                    probability = 1 / (total + 3)
                    # TODO 3-> must be a number of possible values

                total_probability *= probability

            probability_of_classification[classifier] = total_probability
        result = max(probability_of_classification.keys(), key=(lambda k: probability_of_classification[k]))
        return result, expected_output

    def prepare_data(self):
        number_of_rows = len(self.training_set)
        unique_classifiers_dict = defaultdict(list)
        number_of_possible_values = []
        print(self.training_set)
        for row in self.training_set:
            unique_classifiers_dict[row.get(len(row) - 1)].append(row)
        for classifier in unique_classifiers_dict:
            self.probabilities[classifier] = (len(unique_classifiers_dict.get(classifier)) / number_of_rows)
        return unique_classifiers_dict
