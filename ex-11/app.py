from models.world.World import World
from models.world.WorldMap import WorldMap

rows = 15
columns = 15
cell_size = 50
map_file = "./files/world.dat"

world_map = WorldMap(rows, columns, cell_size, map_file)
world = World(world_map)
