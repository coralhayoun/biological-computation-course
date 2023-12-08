from models.world.WorldStatistics import WorldStatistics

class World:
    def __init__(self, world_map):
        self.world_map = world_map
        self.world_statistics = WorldStatistics(world_map.world_matrix)
       

    
    
    
