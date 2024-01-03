import random

def mutation(genome_cells, mutation_rate, mutate_callback):
    mutation_cells = []

    for cell in genome_cells:
        #apply mutation with the specified probability
        if random.random() < mutation_rate:
            mutation_cells.append(mutate_callback(cell))
        else:
            mutation_cells.append(cell)
    
    return mutation_cells