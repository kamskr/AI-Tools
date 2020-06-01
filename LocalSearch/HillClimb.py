

class HillClimb:
    def __init__(self, initial_tour, data_model):
        self.initial_tour = initial_tour
        self.data_model = data_model

    def perform_algorithm(self, method_for_getting_neighbours):
        '''Perform hill climb algorithm'''
        climb = []
        get_length = self.data_model.get_tour_length
        current_best_tour = self.initial_tour
        current_best_distance = get_length(current_best_tour)
        climb.append(-current_best_distance)
        searching_for_best = True
        number_of_iterations = 0

        while searching_for_best:
            new_best_tour = current_best_tour
            new_best_distance = current_best_distance

            for neighbour in method_for_getting_neighbours(current_best_tour):
                distance = get_length(neighbour)
                if distance < current_best_distance:
                    new_best_tour = neighbour
                    new_best_distance = distance

            if current_best_distance != new_best_distance:
                current_best_distance = new_best_distance
                current_best_tour = new_best_tour
                number_of_iterations += 1
                climb.append(-current_best_distance)
            else:
                searching_for_best = False

        current_best_tour.append(current_best_tour[0])
        print("Number of iterations", str(number_of_iterations))
        return current_best_tour, current_best_distance, climb


