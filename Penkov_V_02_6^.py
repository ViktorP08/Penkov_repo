# 1. Дан двумерный массив размером 3x3. Определить максимальное значение среди элементов третьего столбца массива;
# максимальное значение среди элементов второй строки массива. Вывести полученные значения.

arr = [[34, 33, 98], [5, 8, 10], [22, 89, 55]]
max_colonny_tri = arr[0][2]
max_stroki_dva = arr[1][0]
for i in range(len(arr)):
    if arr[i][2] > max_colonny_tri:
        max_colonny_tri = arr[i][2]
for j in range(len(arr[1])):
    if arr[1][j] > max_stroki_dva:
        max_stroki_dva = arr[1][j]
print("Максимальное значение в третьем столбце:", max_colonny_tri)
print("Максимальное значение во второй строке:", max_stroki_dva)

# 2. Дан двумерный массив размером mxn. Сформировать новый массив заменив положительные элементы единицами, а отрицательные нулями. Вывести оба массива.

w = int(input("Пожалуйста, введите число строк: "))
n = int(input("Пожалуйста, введите число столбцов: "))
a = []
for i in range(w):
    b = []
    for j in range(n):
        b.append(int(input()))
    a.append(b)
print("Изначальный массив: \n")
for i in range(w):
    for j in range(n):
        print(a[i][j], end=" ")
    print()
for i in range(w):
    for j in range(n):
        if a[i][j] < 0:
            a[i][j] = 0
        else:
            a[i][j] = 1
print("Конечный массив: \n")
for i in range(w):
    for j in range(n):
        print(a[i][j], end=" ")
    print()


# 3. Дана целая квадратная матрица n-го порядка. Определить, является ли она магическим квадратом, т. е. такой матрицей, 
# в которой суммы элементов во всех строках и столбцах одинаковы.

def w(arr):
    s = sum(arr[0])

    for i in range(len(arr)):
        k = 0
        for j in range(len(arr)):
            k += arr[j][i]
        if k != s or sum(arr[i]) != s:
            return False
    return True


n = int(input("Пожалуйста, введите порядок Вашей матрицы: "))
arr = list()
s = ()
for i in range(n):
    brr = list()
    for i in range(n):
        brr.append(int(input()))
    arr.append(brr)
for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()
print(w(arr))

# 4. Определить, является ли заданная целая квадратная матрица n-го порядка симметричной (относительно главной диагонали)

n = int(input("Пожалуйста, введите порядок Вашей матрицы: "))
arr = list()
s = ()
for i in range(n):
    brr = list()
    for i in range(n):
        brr.append(int(input()))
    arr.append(brr)
for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()
for i in range(0, n - 1):
    for j in range(i + 1, n):
        if arr[i][j] != arr[j][i]:
            s = ("False")
            break
if s != ("False"):
    print("Ваша матрица симметрична")
else:
    print("Ваша матрица обычная")

# 5. Дана прямоугольная матрица. Найти строку с наибольшей и строку с наименьшей суммой элементов. Вывести на печать найденные строки и суммы их элементов.

w = int(input("Пожалуйста, введите число строк: "))
n = int(input("Пожалуйста, введите число столбцов: "))
a = []
k = []
for i in range(w):
    b = []
    for j in range(n):
        b.append(int(input()))
    a.append(b)
for i in range(w):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
for i in range(len(a)):
    k.append(sum(a[i]))
print("Строка, у которой наибольшая сумма: ", a[k.index(max(k))], "Сумма данных элементов: ", max(k))
print("Строка, у которой наименьшая сумма: ", a[k.index(min(k))], "Сумма данных элементов: ", min(k))

# 6.Дана действительная матрица размером n х m, все элементы которой различны. В каждой строке выбирается элемент с наименьшим значением.
# Если число четное, то заменяется нулем, нечетное - единицей. Вывести на экран новую матрицу.

w = int(input("Пожалуйста, введите число строк: "))
n = int(input("Пожалуйста, введите число столбцов: "))
a = []
k = []
for i in range(w):
    b = []
    for j in range(n):
        b.append(int(input()))
    a.append(b)
for i in range(w):
    for j in range(n):
        print(a[i][j], end=" ")
    print()
list = ([(1 if min(i) % 2 else 0) if j == min(i) else j for j in i] for i in a)
for k in list:
    print(k)
