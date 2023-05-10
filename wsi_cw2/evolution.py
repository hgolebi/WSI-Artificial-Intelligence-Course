from random import randrange, gauss

def mutate(individual, sigma):
    new_individual = []
    for x in individual:
        new_individual.append(x + gauss(0, 1) * sigma)
    return new_individual


def reproduce(population, elite_size, function, sigma):
    '''
    population - list of tuples, where:
    x - list element
    x[0] - vector representing individual
    x[1] - value of individual
    '''
    pop_size = len(population)
    population.sort(key=lambda x: x[1])
    new_gen = []
    for it in range(pop_size):
        i = randrange(0, pop_size)
        j = randrange(0, pop_size)
        if population[i][1] > population[j][1]:
            descendant = population[i][0]
        else:
            descendant = population[j][0]
        descendant = mutate(descendant, sigma)
        new_gen.append((descendant, function(descendant)))
    new_gen.sort(key=lambda x: x[1])
    elite = population[-elite_size:]
    for i in range(elite_size):
        new_gen[i] = elite[i]
    return new_gen


def evolutionAlgorithm(population_list, function, elite_size, sigma, if_minimize=False):
    BUDGET = 10000

    if if_minimize:
        temp_fun = function
        function = lambda x: -temp_fun(x)

    population_size = len(population_list)
    population = [(x,function(x)) for x in population_list]
    best = max(population, key=lambda x: x[1])

    for it in range(BUDGET//population_size - 1):
        population = reproduce(population, elite_size, function, sigma)
        if elite_size == 0:
            best = max(best, population[-1], key=lambda x: x[1])

    if elite_size == 0:
        if if_minimize:
            return (best[0], -best[1])
        return best
    else:
        best = max(population, key=lambda x: x[1])
        if if_minimize:
            return (best[0], -best[1])
        return best


