import random

def single_point_crossover(parent1_cells, parent2_cells):
    split_point = random.randint(0, len(parent1_cells))

    return parent1_cells[:split_point] + parent2_cells[split_point:]

def nth_points_crossover(parent1_cells, parent2_cells, n):
    #select n random points
    points = sorted(random.sample(range(len(parent1_cells) + 1), n))

    #perform crossover between the selected points
    child_cells = []
    for i in range(len(points) - 1):
        if i % 2 == 0:
            child_cells += parent1_cells[points[i]:points[i+1]]
        else:
            child_cells += parent2_cells[points[i]:points[i+1]]
    
    return child_cells