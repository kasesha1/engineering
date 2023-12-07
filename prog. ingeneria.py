import math
def x(z):
    return pow(z, 3)-1
def y():
    return math.cos(5)*math.cos(5)
def func(x, y):
    print("Otvet:", x + y)
z = int(input("введите переменную z:"))
func(x(z), y())
