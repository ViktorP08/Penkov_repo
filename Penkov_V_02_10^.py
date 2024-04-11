import numpy as np
import pandas as pd

# 1. Создать объект pandas Series из листа, объекта NumPy, и словаря

w = [1, 2, 3, 4, 5]
series = pd.Series(2)
print("Series из вашего списка:")
print(series)

numpy = np.array([15, 25, 35, 45, 55])
nympyy = pd.Series(numpy)
print("\nSeries из вашего массива:")
print(nympyy)

f = {"q": 100, "w": 200, "e": 300, "r": 400, "t": 500}
seriesd = pd.Series(f)
print("\nSeries из вашего словаря:")
print(seriesd)

# 2. Получить не пересекающиеся элементы в двух объектах Series

series = pd.Series([1, 2, 3, 4, 5])
seriess = pd.Series([4, 5, 6, 7, 8])
print("Элементы series\n", seriess)
print("Элементы seriess\n", series)

r = series[~series.isin(seriess)]._append(seriess[~seriess.isin(series)])
print("Не пересекающиеся элементы:")
print(r)

# 3. Узнать частоту уникальных элементов объекта Series (гистограмма)

w = pd.Series([1, 1, 2, 2, 4, 4, 4, 5, 5])
gist = w.value_counts()

print("Ваша гистограмма")
print(gist)

# 4. Объединить два объекта Series вертикально и горизонтально

series = pd.Series([1, 2, 3])
seriess = pd.Series([4, 5, 6])
vertical = pd.concat([series, seriess], axis=0)
horizontal = pd.concat([series, seriess], axis=1)

print("Вертикальное объединение:")
print(vertical)

print("Горизонтальное объединение:")
print(horizontal)

# 5. Найти разность между объектом Series и смещением объекта Series на n

w = pd.Series([15, 21, 33, 41, 52, 65, 78])

n = 3
razn = w.diff(periods=n)

print("Разность между объектом Series и смещением на", n)
print(razn)