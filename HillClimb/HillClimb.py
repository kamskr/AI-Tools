from data import DataModel
import random


data_model = DataModel()


def init_random_tour():
    tour = list(range(len(data_model.data.get("cities"))))
    random.shuffle(tour)
    return tour


def hill_climb(method_for_getting_neighbours):
    '''Perform hill climb algorithm'''
    get_length = data_model.get_tour_length
    current_best_tour = init_random_tour()
    current_best_distance = get_length(current_best_tour)
    print("starting permutation", str(current_best_tour))

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
        else:
            searching_for_best = False

    print(number_of_iterations)
    return current_best_tour, current_best_distance


best_tour, best_distance = hill_climb(data_model.reversed_sections)
print(best_tour, best_distance)
