from math import atan, tan, log

#Визначення функцій
def fun_1(x):
    return atan(1 / x)

def fun_2(x):
    return tan(x + log(x, 4))

def fun_3(x):
    return 1 / (1 + log(x))

#Табуляція
def tab_func(a, b, h):
    res = []
    x = round(a, 2)

    while x <= b:
        if x < par1:
            y = fun_1(x)
        elif par1 <= x < par2:
            y = fun_2(x)
        else:
            y = fun_3(x)
        res.append((x, y))
        x = round(x + h, 2)
    
    return res



par1 = 1
par2 = 3


h = 0.3
a = 0.3
b = 3.5

tabul = tab_func(a, b, h)

#Вивід результатів
for x, y in tabul:
    print(f'x = {x:.2f}, f(x) = {y:.2f}')
