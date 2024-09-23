import numpy as np
import math

#Визначення функцій
def fun_1(x):
    return math.atan(1 / x)

def fun_2(x):
    return math.tan(x + math.log(x, 4))

def fun_3(x):
    return 1 / (1 + math.log(x))

#Табуляція
def tab_func(a, b, h):
    value_x = np.arange(a, b + h, h)
    res = []

    for x in value_x:
        if x < 1:
            y = fun_1(x)
        elif 1 <= x < 3:
            y = fun_2(x)
        else:
            y = fun_3(x)
        res.append((x, y))
    
    return res


h = 0.3
a = 0.3
b = 3.5

tabul = tab_func(a, b, h)

#Вивід результатів
for x, y in tabul:
    print(f'x = {x:.2f}, f(x) = {y:.2f}')
