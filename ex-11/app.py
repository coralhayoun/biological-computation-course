from models.cell.Cell import Cell
from models.cell.CellParameters import CellParameters
from models.Element import Element

b = CellParameters(Element.LAND, 1, 1, 1)
a = Cell(b)
a.current_parameters.to_string()