import math
z = int(input("Введите z: "))
y = lambda: math.cos(5) * math.cos(5)
x = lambda z: pow(z, 3)-1
func = lambda x, y: x + y
print("otvet:", func(x(z), y()))





