def update_alive_cell(cell, neighbors):
    if not cell.alive:
        return cell
    
    alived_neighbors = sum(neighbor.alive for neighbor in neighbors)
    
    #dies by overpopulation or underpopulation
    if alived_neighbors < 2 or alived_neighbors > 3:
        cell.alive = False
    
    return cell

def keep_dead_cell(cell, neighbors):
    if cell.alive:
        return cell
    
    dead_neighbors = sum(not neighbor.alive for neighbor in neighbors)

    #alive by reproduction
    if dead_neighbors == 3:
        cell.alive = True
    
    return cell

transition_rules = [
    update_alive_cell,
    keep_dead_cell,
]