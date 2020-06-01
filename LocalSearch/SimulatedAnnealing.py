import math
import random


class SimulatedAnnealing:
    def __init__(self, initial_tour, data_model):
        self.initial_tour = initial_tour
        self.data_model = data_model
        self.start_temp = 1000

    def perform_algorithm(self, method_for_getting_neighbours):
        '''Perform Simulated annealing algorithm'''
        climb = []
        get_length = self.data_model.get_tour_length
        current_best_tour = self.initial_tour
        current_best_distance = get_length(current_best_tour)
        climb.append(-current_best_distance)
        number_of_iterations = 0
        same_distances = 0
        temperature_schedule = self.cooling1()

        for temperature in temperature_schedule:
            before_best = current_best_distance
            for neighbour in method_for_getting_neighbours(current_best_tour):
                distance = get_length(neighbour)
                p = self.probability(current_best_distance, distance, temperature)
                new_best_tour = current_best_tour
                new_best_distance = current_best_distance
                if random.random() < p:
                    new_best_tour = neighbour
                    new_best_distance = distance

                current_best_distance = new_best_distance
                current_best_tour = new_best_tour

            if current_best_distance == before_best:
                same_distances += 1
            climb.append(-current_best_distance)

            number_of_iterations += 1
            if same_distances > 4:
                break

        print("Number of iterations", str(number_of_iterations))
        current_best_tour.append(current_best_tour[0])
        return current_best_tour, current_best_distance, climb

    def probability(self, previous_distance, next_distance, temperature):
        if next_distance < previous_distance:
            return 1.0
        else:
            if temperature == 0:
                return 0
            probability = math.exp(-abs(next_distance - previous_distance) / temperature)
            return probability

    def cooling1(self):
        T = self.start_temp
        iteration_number = 0
        while True:
            yield T
            iteration_number += 1
            T *= pow(0.95, iteration_number)
