import math
x = 0.712
y = 3.161

ecuit = (x*y**2 + y*(math.sin(x)) + 142*(x**2)*y)**0.5 + math.tan(x*y) - (142*(y-x))/16.32
print(ecuit)