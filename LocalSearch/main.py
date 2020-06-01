import random
import matplotlib.pyplot as plt
from HillClimb import HillClimb
from SimulatedAnnealing import SimulatedAnnealing
from data import DataModel


data_model = DataModel()

def init_random_tour():
    tour = list(range(len(data_model.data.get("cities"))))
    random.shuffle(tour)
    return tour


initial_tour = init_random_tour()
hill_climb = HillClimb(initial_tour, data_model)

print("Starting permutation", str(initial_tour), "\n")

#Hill climb
best_tour, best_distance, climb = hill_climb.perform_algorithm(data_model.reversed_sections)
print('Best permuttation for reversed method (Hill Climb):', str(best_tour),'Distance:', str(best_distance), '\n')
plt.plot(climb, color = "blue", label="Hill Climb (Reversing method)")
plt.ylabel('Distance')
plt.legend(loc="lower right")

best_tour, best_distance, climb = hill_climb.perform_algorithm(data_model.swapped_cities)
print('Best permuttation for swapping method (Hill Climb):', str(best_tour),'Distance:', str(best_distance), '\n')
plt.plot(climb, color = "green", label="Hill Climb (Swapping method)")
plt.legend(loc="lower right")

# Simulated annealing
simulated_annealing = SimulatedAnnealing(initial_tour, data_model)
print('Starting temperature:', simulated_annealing.start_temp )

best_tour, best_distance, climb = simulated_annealing.perform_algorithm(data_model.reversed_sections)
print('Best permuttation for reversed method (Simulated Annealing):', str(best_tour),'Distance:', str(best_distance), '\n')
plt.plot(climb, color = "red", label="Simulated Annealing (Reversing method)")
plt.legend(loc="lower right")

best_tour, best_distance, climb = simulated_annealing.perform_algorithm(data_model.swapped_cities)
print('Best permuttation for swapping method (Simulated Annealing):', str(best_tour),'Distance:', str(best_distance), '\n')
plt.plot(climb, color = "pink", label="Simulated Annealing (Swapping method)")
plt.legend(loc="lower right")
plt.show()