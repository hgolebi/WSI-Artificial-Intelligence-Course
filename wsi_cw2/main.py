from evolution import evolutionAlgorithm
from random import randint
import numpy as np
from cec2017.functions import f4, f5
from measure import measure
from tabulate import tabulate

UPPER_BOUND = 100
DIMENSIONALITY = 10
POPULATION_SIZE = 200
func = f5

pop = []
for i in range(POPULATION_SIZE):
    pop.append(np.random.uniform(-UPPER_BOUND, UPPER_BOUND, size=DIMENSIONALITY))

for elem in pop:
    print (round(func(elem), 2))

best, value = evolutionAlgorithm(pop, func, 10, 15, True)
print("RESULT: ", round(value, 2))
print([round(x, 2) for x in best])

# pop_results, elite_results, sigma_results = measure(func, 50, 20, 1, 1, [5, 10, 20, 50, 100], [1, 2, 3, 5, 10], [0.2, 0.5, 1, 2, 5, 10], True)

# pop_head = ["population size", "minimum", "maximum", "average", "standard deviation"]
# print(tabulate(pop_results, headers=pop_head, tablefmt="fancy_grid"))

# elite_head = ["elite size", "minimum", "maximum", "average", "standard deviation"]
# print(tabulate(elite_results, headers=elite_head, tablefmt="fancy_grid"))

# sigma_head = ["sigma value", "minimum", "maximum", "average", "standard deviation"]
# print(tabulate(sigma_results, headers=sigma_head, tablefmt="fancy_grid"))