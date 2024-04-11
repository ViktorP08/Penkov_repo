# Поситать значение z по формуле:

import math

print("Введите значение x: ")
x = int(input())
print("Введите значение t: ")
t = int(input())
z = round((9 * (math.pi) * t + 10 * math.cos(x)) / (math.sqrt(t) - abs(math.sin(t))) * math.exp(x), 2)
print(z)
