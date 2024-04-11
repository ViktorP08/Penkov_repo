n = int(input('Введите число овец: '))
while n > 0:
    if n >=2 and n<4:
        print(n, 'овцы')
    elif n==1:
        print(n, 'овца')
    elif n%10 ==1:
        print(n, 'овца')
    elif n>=11 and n<=20:
        print(n, 'Овец')
    elif n==4:
        print(n, 'овцы')
    elif n % 10 > 1 and n % 10 <= 4:
        print(n, 'овцы')
    elif n % 10 == 0 or n % 10 >= 3 and n%10 <= 9 or n%10 == 1:
            print(n, 'овец')
    n -= 1