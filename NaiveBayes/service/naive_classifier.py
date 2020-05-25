from service.csv_parser import CsvParser
from collections import defaultdict


class NaiveClassifier:
    def __init__(self, parser: CsvParser):
        self.training_set = parser.parse_training_set()
        self.test_set = parser.parse_test_set()
        self.probabilities = dict()
        self.unique_classifier_dict, self.number_of_possible_values_per_column = self.prepare_data()
        self.confusion_matrix = {
            "true_positives": 0,
            "false_negatives": 0,
            "false_positives": 0,
            "true_negatives": 0
        }

    def classify(self):
        print(self.number_of_possible_values_per_column)
        total_rows = len(self.test_set)
        correct = 0
        for row in self.test_set:
            result, expected_output = self.classify_row(row)
            if result == expected_output:
                correct += 1
        tp = self.confusion_matrix["true_positives"]
        tn = self.confusion_matrix["true_negatives"]
        fp = self.confusion_matrix["false_positives"]
        fn = self.confusion_matrix["false_negatives"]

        accuracy = (tp + tn)/(tp + tn + fp + fn)
        precision = tp/(tp + fp)
        recall = tp/(tp + fn)
        f1_score = (2 * precision * recall)/(precision + recall)
        print("total rows: ", total_rows, "correct:", correct)
        print("Confusion matrix:", self.confusion_matrix)
        print("Accuracy:", accuracy)
        print("Precision:", precision)
        print("Recall:", recall)
        print("F1 score:", f1_score)


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
                    probability = 1 / (total + self.number_of_possible_values_per_column[i])
                    # TODO 3-> must be a number of possible values
                total_probability *= probability

            probability_of_classification[classifier] = total_probability

        result = max(probability_of_classification.keys(), key=(lambda k: probability_of_classification[k]))

        false_output = list(probability_of_classification.keys())[0]
        if result != false_output and result == expected_output:
            self.confusion_matrix["true_positives"] += 1
        elif result == false_output and expected_output == false_output:
            self.confusion_matrix["true_negatives"] += 1
        elif result == false_output and result != expected_output:
            self.confusion_matrix["false_negatives"] += 1
        elif result != false_output and result != expected_output:
            self.confusion_matrix["false_positives"] += 1
        else:
            print("Some error happened while trying to add to the confusion matrix!")

        print("probability of each class:", probability_of_classification, "**predicted result:", result)
        return result, expected_output

    def prepare_data(self):
        number_of_rows = len(self.training_set)
        unique_classifiers_dict = defaultdict(list)
        number_of_possible_values = defaultdict(set)

        for row in self.training_set:
            for i in range(len(row) - 1):
                number_of_possible_values[i].add(row[i])
            unique_classifiers_dict[row.get(len(row) - 1)].append(row)
        for classifier in unique_classifiers_dict:
            self.probabilities[classifier] = (len(unique_classifiers_dict.get(classifier)) / number_of_rows)
        print(len(number_of_possible_values))

        number_of_values = []
        for value_list in number_of_possible_values.values():
            number_of_values.append(len(value_list))

        return unique_classifiers_dict, number_of_values
