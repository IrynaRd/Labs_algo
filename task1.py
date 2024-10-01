#Визначення функції поділу парної послідовності на збалансовану

def balanced(sequence):
    n = len(sequence)

    left = sequence[:n // 2]
    right = sequence[n // 2:]

    sum_in_left = sum(left)
    sum_in_right = sum(right)

    differ = abs(sum_in_left - sum_in_right)
    print("Найменше число, яке треба додати:", differ)
    
    
    if sum_in_left > sum_in_right:
        right.append(differ)
    else:
        left.append(differ)

    return left, right


#Визначення функції виведення матриці

def balanced_matrix(left, right):
    matrix = [left, right]

    for line in matrix:
        print(line)


sequence = [float(el) for el in input("Введіть через кому парну кількість чисел: ").split(",")]

if len(sequence) % 2 :
    print("Введено послідовність непарного розміру")
else:
    left, right = balanced(sequence)
    balanced_matrix(left, right)