import math
def x(z):
    return lambda: pow(z, 3)-1
def y():
    return lambda: math.cos(5)*math.cos(5)
def func(x, y):
    print("Otvet:", x() + y())
func(x(6), y())





