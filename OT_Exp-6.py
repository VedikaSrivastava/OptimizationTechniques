# -*- coding: utf-8 -*-
"""
Created on Wed May 12 00:09:22 2021

@author: vedika
"""

import numpy as np

def select_mating_pool(pop, fitness, num_parents):
    # Selecting the best individuals in the current generation as parents
    parents = np.empty((num_parents, pop.shape[1]))
    for parent_num in range(num_parents):
        max_fitness_idx = np.where(fitness == np.max(fitness))
        max_fitness_idx = max_fitness_idx[0][0]
        parents[parent_num, :] = pop[max_fitness_idx, :]
        fitness[max_fitness_idx] = float('-inf')
    return parents

def crossover(parents, offspring_size):
    offspring = np.empty(offspring_size)
    crossover_point = np.uint8(offspring_size[1]/2) #center as crossover point
    for k in range(offspring_size[0]):
        parent1_idx = k % parents.shape[0]
        parent2_idx = (k+1) % parents.shape[0]
        offspring[k, 0:crossover_point] = parents[parent1_idx, 0:crossover_point]
        offspring[k, crossover_point:] = parents[parent2_idx, crossover_point:]
    return offspring

def mutation(offspring_crossover, num_mutations=1):
    mutations_counter = np.uint8(offspring_crossover.shape[1] / num_mutations)
    for idx in range(offspring_crossover.shape[0]):
        gene_idx = mutations_counter - 1
        for mutation_num in range(num_mutations):
            random_value = np.random.uniform(-1.0, 1.0, 1)
            offspring_crossover[idx, gene_idx] = offspring_crossover[idx, gene_idx] + random_value
            gene_idx = gene_idx + mutations_counter
    return offspring_crossover


weight_ip = list(map(float,input("Enter the weights (give space between each value):").strip().split()))
n_opt = 5 # Number of the x terms to be optimize.

chromo_per_pop = 7 # Number of chromosomes per population
pop_size = (chromo_per_pop,n_opt) # Population size
population = np.random.uniform(low=-4.0, high=4.0, size=pop_size) # Initial population

num_parents_mating = 4

fitness = np.sum(population*weight_ip,  axis=1)
print("\n\nFitness values:\n",fitness)
parents = select_mating_pool(population, fitness, num_parents_mating) #best parents
print("\nSelected Parents:\n",parents)
offspring_crossover = crossover(parents, offspring_size=(pop_size[0]-parents.shape[0], n_opt))
print("\nCross-over Result:\n",offspring_crossover)
offspring_mutation = mutation(offspring_crossover)
print("\nMutation Result:\n",offspring_mutation)
population[0:parents.shape[0], :] = parents
population[parents.shape[0]:, :] = offspring_mutation

print("\nBest result(maximum): ", np.max(np.sum(population*weight_ip, axis=1)))


"""
------------------------------------------------------------------------------
IMPLEMENTING GA USING LIBRARY FUNCTION
"""
from geneticalgorithm import geneticalgorithm as ga

def f(X):
    return (-1 * np.sum(X * weight_ip))

varbound=np.array([[0,31]]*5)

model=ga(function=f,dimension=5,variable_type='real',variable_boundaries=varbound)
print("\n\n------------------------------\nOUTPUT using LIBRARY FUNCTION\n")

model.run()
print(model.param)
