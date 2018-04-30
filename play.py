from imageProcessor import MapProcessor as proc
from solver import Solver as sol

map_name = "maps/map4.png"


processor = proc(map_name)
print("image processing...")
array = processor.make_processing()

print(array)
print("solving sudoku...")
solver = sol()
solver.solve(array)
result = solver.get_solve()
print('------solved--------')
print(result)