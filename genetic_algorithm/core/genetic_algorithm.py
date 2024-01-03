import random

class GeneticAlgorithm:
    def __init__(self, population, fitness_calculation, crossover_function, mutation_function, max_generation):
        self.population = population
        self.population_size = len(population)

        self.fitness_calculation = fitness_calculation
        self.crossover_function = crossover_function
        self.mutation_function = mutation_function

        self.current_generation = 0
        self.max_generation = max_generation

    def run_algorithm_iteration(self):
        sorted_population = sorted(self.population, key = self.fitness_calculation, reverse = True)
        best_fitness = self.fitness_calculation(sorted_population[0])

        new_population = [sorted_population[0]]

        for i in range(self.population_size):
            # Select parents from the top performers
            parent1 = random.choice(sorted_population[:5])
            parent2 = random.choice(sorted_population[:5])

            child = self.crossover_function(parent1, parent2)
            child = self.mutation_function(child)
            
            new_population.append(child)

    