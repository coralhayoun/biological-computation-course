from models.automaton.cell.cell_wind import WindDirection

reverse_wind_directions = {
    WindDirection.NORTH.name: WindDirection.SOUTH,
    WindDirection.SOUTH.name: WindDirection.NORTH,
    WindDirection.EAST.name: WindDirection.WEST,
    WindDirection.WEST.name: WindDirection.EAST
}