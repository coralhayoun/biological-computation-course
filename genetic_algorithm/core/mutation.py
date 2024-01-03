import random

def mutation(genome_cells, mutation_rate):
    mutation_cells = []

    for cell in genome_cells:
        #apply mutation with the specified probability
        if random.randint(1,10) < mutation_rate * 10:
            mutation_cells.append(cell)
        else:
            mutation_cells.append(cell)
    
    return mutation_cells