import numpy as np

def cum_sum(x, d):
    n = 1
    sum = 0
    elem = x

    while abs(elem) > d:
        sum -= elem
        n += 1
        elem =(x ** (n + 1)) / (n + 1)

    return sum

#Табулювання 
def tab_cumsum(a, b, h, d):
    value_x = np.arange(a, b + h, h)
    res = []

    for x in value_x:
        y = cum_sum(x, d)
        res.append((x, y))

    return res


a = -0.5
b = 0.0
h = 0.05
d = 0.001

res = tab_cumsum(a, b, h, d)

for x, y in res:
    print(f"x = {x: .3f}, f(x) = {y: .3f}")

