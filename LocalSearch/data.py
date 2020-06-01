import random


class DataModel:
    def __init__(self):
        self.data = self.create_data_model()

    def create_data_model(self):
        """Stores the data for the problem."""
        data_dict = dict()
        data_dict['cities'] = ["New York", "Los Angeles", "Chicago", "Minneapolis", "Denver", "Dallas", "Seattle",
                               "Boston", "San Francisco", "St. Louis", "Houston", "Phoenix", "Salt Lake City"]

        data_dict['distance_matrix'] = [
            [0, 2451, 713, 1018, 1631, 1374, 2408, 213, 2571, 875, 1420, 2145, 1972],
            [2451, 0, 1745, 1524, 831, 1240, 959, 2596, 403, 1589, 1374, 357, 579],
            [713, 1745, 0, 355, 920, 803, 1737, 851, 1858, 262, 940, 1453, 1260],
            [1018, 1524, 355, 0, 700, 862, 1395, 1123, 1584, 466, 1056, 1280, 987],
            [1631, 831, 920, 700, 0, 663, 1021, 1769, 949, 796, 879, 586, 371],
            [1374, 1240, 803, 862, 663, 0, 1681, 1551, 1765, 547, 225, 887, 999],
            [2408, 959, 1737, 1395, 1021, 1681, 0, 2493, 678, 1724, 1891, 1114, 701],
            [213, 2596, 851, 1123, 1769, 1551, 2493, 0, 2699, 1038, 1605, 2300, 2099],
            [2571, 403, 1858, 1584, 949, 1765, 678, 2699, 0, 1744, 1645, 653, 600],
            [875, 1589, 262, 466, 796, 547, 1724, 1038, 1744, 0, 679, 1272, 1162],
            [1420, 1374, 940, 1056, 879, 225, 1891, 1605, 1645, 679, 0, 1017, 1200],
            [2145, 357, 1453, 1280, 586, 887, 1114, 2300, 653, 1272, 1017, 0, 504],
            [1972, 579, 1260, 987, 371, 999, 701, 2099, 600, 1162, 1200, 504, 0],
        ]

        return data_dict

    def get_tour_length(self, tour: [int]):
        total = 0
        distance_matrix = self.data.get('distance_matrix')
        num_cities = len(tour)
        for i in range(num_cities):
            j = (i + 1) % num_cities
            city_i = tour[i]
            city_j = tour[j]
            total += distance_matrix[city_i][city_j]
        return total

    def all_possible_pairs(self, shuffle=random.shuffle):
        """Random pairs generator."""
        size = len(self.data.get('cities')) - 1
        r1 = list(range(size))
        r2 = list(range(size))
        if shuffle:
            shuffle(r1)
            shuffle(r2)
        for i in r1:
            for j in r2:
                yield i, j

    def swapped_cities(self, tour: [int]):
        '''Generator to create all possible variations
          where two cities have been swapped'''
        for i, j in self.all_possible_pairs():
            if i < j:
                copy = tour[:]
                copy[i], copy[j] = tour[j], tour[i]
                yield copy

    def reversed_sections(self, tour: [int]):
        '''generator to return all possible variations
          where the section between two cities are swapped'''
        for i, j in self.all_possible_pairs():
            if i != j:
                copy = tour[:]
                if i < j:
                    copy[i:j + 1] = reversed(tour[i:j + 1])
                else:
                    copy[i + 1:] = reversed(tour[:j])
                    copy[:j] = reversed(tour[i + 1:])
                if copy != tour:  # no point returning the same tour
                    yield copy