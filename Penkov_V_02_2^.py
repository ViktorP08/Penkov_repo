# 1. Написать программу, которая будет делить введенные пользователем два вещественных числа и выводить результат на экран, сообщая об ошибке в случае деления на ноль.

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
if b == 0:
    print("Ошибка, делить на 0 запрещено")
else:
    print("Результат: ", a / b)

# 2.Рассчитать стоимость покупки с учетом скидки в 35%, которая предоставляется покупателю, если сумма покупки превышает 20 у.е. Сумму покупки ввести с клавиатуры, а результаты округлить до сотых (копейки, центы и т.д.). Вывести на экран итоговую стоимость и размер предоставленной скидки.

a = int(input("Введите сумму покупки: "))
if a > 20:
    b = a - a * 0.65
    a *= 0.65
    print("Скидка составляет: ", round(b, 2), "Итоговая сумма: ", round(a, 2))
else:
    print("Итоговая сумма меньше 20, этого недостаточно для скидки, Ваша сумма покупки: ", a)


# 3. Напишите скрипт, который по введенному пользователем числу от 1 до 12, будет выводить на экран сообщение в виде названия месяца и времени года. Если пользователь введет недопустимое число, программа должна выдавать сообщение об ошибке.

def qq(a):
    if a == 1 or a == 2 or a == 12:
        if a == 1:
            print("Месяц: Январь, время года: Зима")
        elif a == 2:
            print("Месяц: Февраль,время года: Зима")
        elif a == 12:
            print("Месяц: Декабрь, время года: Зима")
    if a == 3 or a == 4 or a == 5:
        if a == 3:
            print("Месяц: Март, время года: Осень")
        elif a == 4:
            print("Месяц: Апрель, время года: Осень")
        elif a == 5:
            print("Месяц: Май, время года: Осень")
    if a == 6 or a == 7 or a == 8:
        if a == 6:
            print("Месяц: Июнь, время года: Лето")
        elif a == 7:
            print("Месяц: Июль, время года: Лето")
        elif a == 8:
            print("Месяц: Август, время года: Лето")
    if a == 9 or a == 10 or a == 11:
        if a == 6:
            print("Месяц: Сентябрь, время года: Осень")
        elif a == 7:
            print("Месяц: Октябрь, время года: Осень")
        elif a == 8:
            print("Месяц: Ноябрь, время года: Осень")
    if a > 12 or a < 1:
        print("Ошибка, введите другое число")


a = int(input("Введите номер месяца: "))
qq(a)