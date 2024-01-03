import random

from core.population import Population

class GeneticAlgorithm:
    def __init__(self, population, fitness_calculation, crossover_function, mutation_function, max_generation):
        self.fitness_calculation = fitness_calculation
        self.crossover_function = crossover_function
        self.mutation_function = mutation_function

        self.population = population
        self.population_size = len(population)
        self.update_population(self.population)

        self.current_generation = 0
        self.max_generation = max_generation

    def run_algorithm(self):
        while self.current_generation <= self.max_generation:
            print("running {} generation".format(self.current_generation))
            self.run_algorithm_iteration()
            print("\nDONE iteration")  

        best = self.get_fittest_cell()
        return best

    def run_algorithm_iteration(self):
        (chromosomes_list, probabilities_list) = self.extract_population_data(self.population)
        new_population = []

        print("\ncreating and running simulation for {} offsprings: ".format(self.population_size), end='')
        for _ in range(self.population_size):
            new_cell = self.create_offspring(chromosomes_list, probabilities_list)
            new_population.append(new_cell)
        
        self.update_population(new_population)
        self.population = new_population
        self.current_generation += 1
        
    def create_offspring(self, chromosomes_list, probabilities_list):
        ancestors_number = random.randint(1,2)
        picked_parents = random.choices(chromosomes_list, weights = probabilities_list, k = ancestors_number)
        child = picked_parents[0]

        if ancestors_number == 2:
            child = self.crossover_function(picked_parents[0], picked_parents[1])
            
        child = self.mutation_function(child)

        return Population(child)

    def update_population(self, population):
        fitness_sum = 0
        for i in range(len(population)):
            fitness = self.fitness_calculation(population[i].chromosome)
            population[i].fitness = fitness
            fitness_sum += fitness
        
        for i in range(len(population)):
            probability = population[i].fitness / fitness_sum
            population[i].probability = probability
    
    def extract_population_data(self, population):
        chromosomes_list = []
        probabilities_list= []

        for i in range(len(population)):
            chromosomes_list.append(population[i].chromosome)
            probabilities_list.append(population[i].probability)
        
        return (chromosomes_list, probabilities_list)
    
    def get_fittest_cell(self):
        fittest_cell = self.population[0]

        for i in range(len(self.population)):
            if(self.population[i].fitness > fittest_cell.fitness):
                fittest_cell = self.population[i]
        
        return fittest_cell


    