class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __sub__(self, other):
        matrix_in_res = []
        for i in range(len(self.matrix)):
            new_raw = []
            for j in range(len(self.matrix[i])):
                new_raw.append(self.matrix[i][j] - other.matrix[i][j])
            matrix_in_res.append(new_raw)
        return Matrix(matrix_in_res)

    def __str__(self):
        res = ""
        for raw in self.matrix:
            res += "[" + ", ".join(str(el) for el in raw) + "]\n"
        return res

    def sort(self, func):
        def sorted_matrix(*args, **kwargs):
            sorted_matrix = []
            for raw in self.matrix:
                copied_raw = raw[:]
                n = len(raw)
                for i in range(n):
                    for j in range(n - i - 1):
                        if copied_raw[j] < copied_raw[j + 1]:
                            copied_raw[j], copied_raw[j + 1] = copied_raw[j + 1], copied_raw[j]
                sorted_matrix.append(copied_raw)
            print("Sorted matrix:")
            for raw in sorted_matrix:
                print(raw)
            return func(sorted_matrix, *args, **kwargs)
        return sorted_matrix
    
    
    def multiply_column(self, matrix = None):
        if matrix is None:
            matrix = self.matrix

        ln = len(matrix)
        multiplied = []
        for col in range(ln):
            result = 1
            for raw in range(col + 1, ln):
                result *= matrix[raw][col]
            if result == 1:
                result = 0
            multiplied.append(result)
        print("Products of columns under the main diagonal:")
        print(multiplied)
        return multiplied
    

    def arithmetic_mean_for_multiplied(self, multiplied):
        if len(multiplied) == 0:
            return 0
        return sum(multiplied) / len(multiplied)
    

matrix1 = [[19, 62, -45, -1, 84],
          [23, 54, -4, -2, 68],
          [36, 39, 96, 94, 97],
          [-3, -8, -4, -6, -22],
          [98, -5, -3, 0, 11]]

matrix2 = [[22, 41, 45, -45, -49], 
          [5, 1, 3, -2, 0], 
          [34, 97, 48, 72, -1],
          [-3, -7, 5, 92, 20], 
          [0, -3, -57, 9, 1]]

matrix_object = Matrix(matrix1)
matrix_object_2 = Matrix(matrix2)
result_matrix = matrix_object - matrix_object_2
print("Result matrix: ")
print(result_matrix)



print("For original matrix1: ")
products_original = matrix_object.multiply_column()
print("Arithmetic mean of products: ", matrix_object.arithmetic_mean_for_multiplied(products_original))


print("\nFor sorted matrix1:")
@matrix_object.sort
def multiply_col_decorated(matrix):
    return matrix_object.multiply_column(matrix)

products_sorted = multiply_col_decorated()
print("Arithmetic mean of products in sorted_matrix:", matrix_object.arithmetic_mean_for_multiplied(products_sorted))








