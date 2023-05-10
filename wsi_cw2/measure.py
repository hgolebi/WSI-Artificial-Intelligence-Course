from evolution import evolutionAlgorithm
import numpy as np
from statistics import stdev
from tabulate import tabulate


def measure(function, iterations, base_popsize, base_elitesize, base_sigma, popsize_list, elitesize_list, sigma_list, if_minimize=False):
    UPPER_BOUND = 100
    DIMENSIONALITY = 10

    # POMIARY WPŁYWU WIELKOSCI POPULACJI
    popsize_results = []
    for popsize in popsize_list:
        results = []
        for it in range(iterations):
            pop = []
            for i in range(popsize):
                pop.append(np.random.uniform(-UPPER_BOUND, UPPER_BOUND, size=DIMENSIONALITY))
            best, value = evolutionAlgorithm(pop, function, base_elitesize, base_sigma, if_minimize)
            results.append(value)
        avg = round(sum(results) / len(results), 2)
        mini = round(min(results), 2)
        maxi = round(max(results), 2)
        std = round(stdev(results), 2)
        popsize_results.append([popsize, mini, maxi, avg, std])

    # POMIARY WPŁYWU WIELKOSCI ELITY
    elitesize_results = []
    for elitesize in elitesize_list:
        results = []
        for it in range(iterations):
            pop = []
            for i in range(base_popsize):
                pop.append(np.random.uniform(-UPPER_BOUND, UPPER_BOUND, size=DIMENSIONALITY))
            best, value = evolutionAlgorithm(pop, function, elitesize, base_sigma, if_minimize)
            results.append(value)
        avg = round(sum(results) / len(results), 2)
        mini = round(min(results), 2)
        maxi = round(max(results), 2)
        std = round(stdev(results), 2)
        elitesize_results.append([elitesize, mini, maxi, avg, std])

    # # POMIARY WPŁYWU SIŁY MUTACJI
    sigma_results = []
    for sigma in sigma_list:
        results = []
        for it in range(iterations):
            pop = []
            for i in range(base_popsize):
                pop.append(np.random.uniform(-UPPER_BOUND, UPPER_BOUND, size=DIMENSIONALITY))
            best, value = evolutionAlgorithm(pop, function, base_elitesize, sigma, if_minimize)
            results.append(value)
        avg = round(sum(results) / len(results), 2)
        mini = round(min(results), 2)
        maxi = round(max(results), 2)
        std = round(stdev(results), 2)
        sigma_results.append([sigma, mini, maxi, avg, std])

    return popsize_results, elitesize_results, sigma_results