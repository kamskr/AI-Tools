from service.csv_parser import CsvParser

parser = CsvParser("./data/car.data", "./data/car.test.data")

parser.parse_test_set()