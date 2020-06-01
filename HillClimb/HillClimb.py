from data import DataModel
import random
import matplotlib.pyplot as plt


data_model = DataModel()

def init_random_tour():
    tour = list(range(len(data_model.data.get("cities"))))
    random.shuffle(tour)
    return tour


def hill_climb(method_for_getting_neighbours, initial_tour):
    '''Perform hill climb algorithm'''
    climb = []
    get_length = data_model.get_tour_length
    current_best_tour = initial_tour
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

    print("Number of iterations", str(number_of_iterations))
    return current_best_tour, current_best_distance, climb

initial_tour = init_random_tour()
print("Starting permutation", str(initial_tour), "\n")
best_tour, best_distance, climb = hill_climb(data_model.reversed_sections, initial_tour)
print('Best permuttation for reversed method:', str(best_tour),'Distance:', str(best_distance))
plt.plot(climb, color = "blue", label="Reversing method")
plt.ylabel('Distance')
plt.legend(loc="upper left")
best_tour, best_distance, climb = hill_climb(data_model.swapped_cities, initial_tour)
print('Best permuttation for swapping method:', str(best_tour),'Distance:', str(best_distance))
plt.plot(climb, color = "green", label="Swapping method")
plt.legend(loc="upper left")
plt.show()
