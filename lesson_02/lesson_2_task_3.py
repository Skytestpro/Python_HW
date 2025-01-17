import math


def square(x):
    return math.ceil(x * x)


z = float(input("Введите сторону квадрата: "))
print(f"Площадь квадрата: {square(z)}")
