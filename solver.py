import numpy as np
test_array = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
              [6, 0, 0, 1, 9, 5, 0, 0, 0],
              [0, 9, 8, 0, 0, 0, 0, 6, 0],
              [8, 0, 0, 0, 6, 0, 0, 0, 3],
              [4, 0, 0, 8, 0, 3, 0, 0, 1],
              [7, 0, 0, 0, 2, 0, 0, 0, 6],
              [0, 6, 0, 0, 0, 0, 2, 8, 0],
              [0, 0, 0, 4, 1, 9, 0, 0, 5],
              [0, 0, 0, 0, 8, 0, 0, 7, 9]]



class Solver:

    def __init__(self):
        self.solved = []

    def solve(self, array):
        iters = len(array)
        for i in range(iters):
            for j in range(iters):
                if array[i][j] == 0:
                    for v in range(1, 10):
                        if self.value_is_possible(array, v, i, j):
                            array[i][j] = v
                            self.solve(array)
                            if self.check_if_done(array):
                                self.solved = array.copy()
                                return array

                        if v == 9:
                            array[i][j] = 0
                            return array
            # print(array)
            # print("------")
        return array

    def value_is_possible(self, array, value, row, col):
        if self.check_column(array, value, col) == False:
            if self.check_row(array, value, row) == False:
                if self.check_box(array, value, col, row) == False:
                    return True
        return False

    def check_row(self, array, val, row):#True - exist in row
        return val in array[row]

    def check_column(self, array, val, column): #True - exist in column
        for i in range(len(array)):
            if val == array[i][column]:
                return True
        return False

    def check_box(self, array, val, column, row):#True - value in box
        vals = self.get_values_form_box(array,column, row)
        return val in vals


    def get_values_form_box(self,array, column, row):
        x_box = int(column / 3)
        y_box = int(row / 3)
        all_vals_from_box = []
        for i in range(3):
            y = y_box * 3 + i
            for j in range(3):
                x = x_box * 3 + j
                array_val = array[y][x]
                if array_val != 0:
                    all_vals_from_box.append(array_val)
        return all_vals_from_box

    def check_if_done(self, array):#True - done
        for i in range(len(array)):
            if 0 in array[i]:
                return False
        return True
    def get_solve(self):
        res = np.array(self.solved)
        # res = np.reshape(res, (9,9))
        return res

# solver = Solver()
# # vals = solver.get_values_form_box(test_array,2,1)
# # print(vals)
# print(np.reshape(np.asarray(test_array), newshape=(9,9)))
# print('----solve------')
#
# print(np.reshape(np.asarray(solver.solve(test_array)), newshape=(9,9)))
# res = solver.get_solve()
#
# print(res)
