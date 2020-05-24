from service.csv_parser import CsvParser
from service.naive_classifier import NaiveClassifier

parser = CsvParser("./data/car.data", "./data/car.test.data")
classifier = NaiveClassifier(parser)
classifier.classify_row(classifier.test_set[1])