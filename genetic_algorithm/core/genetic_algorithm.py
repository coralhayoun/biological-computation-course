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

    def run_algorithm(self):
        while self.current_generation < self.max_generation:
            self.run_algorithm_iteration()

        sorted_population = sorted(self.population, key = self.fitness_calculation, reverse = True)
        best = sorted_population[0]
        return best

    def run_algorithm_iteration(self):
        sorted_population = sorted(self.population, key = self.fitness_calculation, reverse = True)
        print("new iteration began {}".format(self.current_generation))
        new_population = sorted_population[0:2]

        for _ in range(self.population_size - 2):
            new_cell = self.create_offspring(sorted_population)
            new_population.append(new_cell)
        
        self.population = new_population
        self.current_generation += 1
        
    
    def create_offspring(self, sorted_population):
        # Select parents from the top performers
        parent1 = random.choice(sorted_population[:5])
        parent2 = random.choice(sorted_population[:5])

        child = self.crossover_function(parent1, parent2)
        child = self.mutation_function(child)

        return child

    