from service.csv_parser import CsvParser
from collections import defaultdict


class NaiveClassifier:
    def __init__(self, parser: CsvParser):
        self.training_set = parser.parse_training_set()
        self.test_set = parser.parse_test_set()
        self.probabilities = dict()
        self.unique_classifier_dict = self.prepare_data()

    def classify(self):
        print()

    def classify_row(self, row: dict):
        probability_of_classification = dict()
        expected_output = row[len(row) - 1]
        for classifier in self.probabilities:
            probability_given_classifier = []
            for i in range(len(row) - 1):
                counter = 0
                total = 0
                for row_in_unique_classifier in self.unique_classifier_dict[classifier]:
                    if row[i] == row_in_unique_classifier[i]:
                        counter += 1
                        total += 1
                    else:
                        total += 1
                probability_given_classifier.append(counter/total)
            probability_of_classification[classifier] = probability_given_classifier

        print(probability_of_classification)






    def prepare_data(self):
        number_of_rows = len(self.training_set)
        unique_classifiers_dict = defaultdict(list)
        for row in self.training_set:
            unique_classifiers_dict[row.get(len(row) - 1)].append(row)

        for classifier in unique_classifiers_dict:
            self.probabilities[classifier] = (len(unique_classifiers_dict.get(classifier))/number_of_rows)

        return unique_classifiers_dict