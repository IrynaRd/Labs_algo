matrix = [[19, 62, -45, -1, 84],
          [23, 54, -4, -2, 68],
          [36, 39, 96, 94, 97],
          [-3, -8, -4, -6, -22],
          [98, -5, -3, 0, 11]]

def sort_matrix(matrix):
    sorted_matrix = []
    for raw in matrix:
        n = len(raw)
        for i in range(n):
            for j in range(n - i - 1):
                if raw[j] < raw[j + 1]:
                    raw[j], raw[j + 1] = raw[j + 1], raw[j]
        sorted_matrix.append(raw)
    print("Sorted matrix:")
    for raw in sorted_matrix:
        print(raw)
    
sort_matrix(matrix)        
            
def multiply_column(matrix):
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

products = multiply_column(matrix)

def arithmetic_mean_for_multiplied(multiplied):
    if len(multiplied) == 0:
        return 0
    return sum(products) / len(products)


arithm_average = arithmetic_mean_for_multiplied(products)
print("Arithmetic mean of products: ", arithm_average)
