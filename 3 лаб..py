def zd1():
    a = int(input("Введите число,которое нужно проверить на деление на 3: "))
    if a % 3 == 0:
        print("Число делится на 3!")
    else:
        print("Число НЕ делится на 3...")

def zd2():
    try:
        b = 100
        a = int(input("Введите число,на которое будем делить 100: "))
        if b % a == 0:
          print("100 делится на число " , a)
        else:
           print("100 НЕ делится на число ", a)
    except ValueError:
        print("Похоже,вы ввели не число/цифру,пожалуйста,введите только число")
    except ZeroDivisionError:
        print("Деление на ноль невозможно")
#1 вариант решения 3 задачи
def zd31():
    a = int(input("Введите день: "))
    b = int(input("Введите номер месяца: "))
    c = input("Введите год: ")

    d = int(c[-2:])

    if a * b == d:
        print("Дата магическая!")
    else:
        print("Дата НЕ магическая...")

#2 вариант решения 3 задачи
def zd32():
    from datetime import datetime
    date_str = input("Введите дату в формате ДД-ММ-ГГГГ: ")

    date = datetime.strptime(date_str, "%d-%m-%Y")
    print(date)
    a = int(date.day)
    b = int(date.month)
    c = date.year
    print(a , b , c)
    c = int(str(c)[-2:])
    if a * b == c:
        print("Дата магическая!")
    else:
        print("Дата НЕ магическая...")
#вариант с шестизначным номером билета
def zd41():
    a = str(input("Введите номер билета: "))
    n = a.split()
    d = a[0] + a[1] + a[2]
    c = a[3] + a[4] + a[5]
    r = sum(map(int, d))
    v = sum(map(int, c))
    if r == v:
        print("билет счастливый!")
    else:
        print("билет  не счастливый!")
#вариант с любой длиной номера билета
def zd42():
    a = str(input("Введите номер билета с четным кол-вом цифр: "))
    l = len(a)
    print("Количество цифр в числе: " ,l)
    if l % 2 != 0:
        print("Введен номер из нечетного кол-ва цифр")
    else:
        x = int(l / 2)
        b = sum(map(int, a[:x]))
        d = sum(map(int, a[x:]))
        print("Сумма первой половины цифр: " , b)
        print("Сумма второй половины цифр: " ,d)
        if b == d:
            print("билет счастливый!")
        else:
            print("билет  не счастливый!")

zd1()