#Визначення функції
def cum_sum(x, d):
    n = 1
    sum = 0
    elem = x

    while abs(elem) > d:
        sum -= elem
        n += 1
        elem =(x ** (n + 1)) / (n + 1)

    return sum

#Табуляція 
def tab_cumsum(a, b, h, d):
    res = []
    x = round(a, 2)

    while x <= b:
        fun_y = cum_sum(x, d)
        res.append((x, fun_y))
        x = round(x + h, 3)

    return res

a = -0.5
b = 0.0
h = 0.05
d = 0.001

res = tab_cumsum(a, b, h, d)

#Вивід результатів
for x,  fun_y in res:
    print(f"x = {x: .3f}, f(x) = {fun_y: .3f}")

