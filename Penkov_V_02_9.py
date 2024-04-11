# 3. Построить в общих осях графики для x<0.
# На том же графике сделать 1 врезку, демонстрирующую поведение графиков при удалении x от 0 к −∞.
# Необходимо продемонстрировать возможность (или невозможность) пересечений и стремление функций. Так же нанесите на графики прямую f(x) = 0.
# Цвет линий на врезках и основном графике должен быть одинаковым для одних и тех же значений α и β.

from matplotlib import pyplot as plt
import math
import numpy as np


def w(i, a, b):
    return (pow(i, b) + pow(a, b)) / pow(i, b)


def graph(a, b, color):
    x = []
    y = []
    for i in range(-250, 250):
        if i == 0:
            x.append(float(np.inf))
            y.append(float(np.inf))
            continue
        x.append(i)
        y.append(w(i, a, b))
    plt.plot(x, y, color)


plt.legend()

graph(1, 1, "blue")
graph(2, 1, "red")
graph(1, 2, "green")
plt.xlabel("ОСЬ Х")
plt.ylabel("ОСЬ У")
plt.title(r"$f(x) = \frac{x^\beta+\alpha^\beta}{x^\beta}$")
plt.grid()
plt.legend(["a=1,  b=1", "a=2, b=1", "a=1, b=1"])
plt.show()


# 4. Построить в общих осях графики для:
# α=1,β=0.5
# α=1,β=−0.5
# α=1,β=−1.5
# Сделайте выводы о поведении графиков, включая возрастание/убывание и выпуклость/вогнутость
# В результате выполнения предыдущей задачи, вы вероятно заметите, что все графики с α=1 проходят через общую точку (1, 2).
# Постройте в одном ряду 3 графика, чтобы убедиться в выводах, сделанных по результатам предыдущей задачи.
# α=1,β=0.5 
# α=1,β=0.8
# α=1,β=−0.5 
# α=1,β=−0.8
# α=1,β=−1.5 
# α=1,β=−2.5

def w(i, a, b):
    return (pow(i, b) + pow(a, b)) / pow(i, b)


def graph(a, b, color):
    x = []
    y = []
    for i in range(-250, 250):
        if i == 0:
            x.append(float(np.inf))
            y.append(float(np.inf))
            continue
        x.append(i)
        y.append(w(i, a, b))
    plt.plot(x, y, color)


plt.legend()
graph(1, 0.5, "red")
graph(1, -0.5, "seagreen")
graph(1, -1.5, "navy")
plt.xlabel("ОСЬ Х")
plt.ylabel("ОСЬ У")
plt.title(r"$f(x) = \frac{x^\beta+\alpha^\beta}{x^\beta}$")
plt.grid()
plt.legend(["a=1,  b=0.5", "a=1, b=-0.5", "a=1, b=-1.5"])
plt.show()


def w(i, a, b):
    return (pow(i, b) + pow(a, b)) / pow(i, b)


def graph(a, b, color):
    x = []
    y = []
    for i in range(-250, 250):
        if i == 0:
            x.append(float(np.inf))
            y.append(float(np.inf))
            continue
        x.append(i)
        y.append(w(i, a, b))
    plt.plot(x, y, color)


plt.legend()
graph(1, 0.5, "darkgreen")
graph(1, 0.8, "darkgreen")
graph(1, -0.5, "crimson")
graph(1, -0.8, "crimson")
graph(1, -1.5, "slateblue")
graph(1, -2.5, "slateblue")
plt.xlabel("ОСЬ Х")
plt.ylabel("ОСЬ Х")
plt.title(r"$f(x) = \frac{x^\beta+\alpha^\beta}{x^\beta}$")
plt.grid()
plt.legend(["a=1,  b=0.5", "a=1, b=0.8", "a=1, b=-0.5", "a=1, b=-0.8", "a=1, b=-1.5", "a=1, b=-2.5"])
plt.show()
