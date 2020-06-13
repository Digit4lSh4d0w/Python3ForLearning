from math import sin

def threeSides():
    a, b, c = list(map(int, input('\nВведите величины 3 сторон через пробел: ').split()))
    p = (a + b + c) // 2
    s = round((p * (p - a) * (p - b) * (p - c)) ** 0.5)
    # print('S %s | P %s '%(s, p))
    if s % 2 == 0:
        return s
    else:
        return 'Не могу делить на 2'

def heightAndGround():
    b, h = list(map(int, input('\nВведите величину сначала основание, а затем высоты через пробел: ').split()))
    s = round((b * h) // 2)
    # print('S %s '%(s))
    if s % 2 == 0:
        return s
    else:
        return 'Не могу делить на 2'

def sideAndCorner():
    a, b, c = list(map(int, input('\nВведите величины сторон и угла между ними через пробел: ').split()))
    s = 0.5 * a * b * round(sin(c))
    # print('S %s | Sin %s'%(s, round(sin(c))))
    if s % 2 == 0:
        return s
    else:
        return 'Не могу делить на 2'


while True:
    print('''Выберите способ нахождения площади треугольника:

    1. По 3 сторонам.
    2. Через основание и высоту.
    3. Через стороны и угол между ними.\n''')
    opt = int(input('~~~> '))
    if opt == 1:
        print('\nОтвет # %s \n'%(threeSides()))
    elif opt == 2:
        print('\nОтвет # %s \n'%(heightAndGround()))
    elif opt == 3:
        print('\nОтвет # %s \n'%(sideAndCorner()))
    else:
        print('\n\n\nНу я в шоке ... 3 цифры = 3 варианта ... Давайте как будто этого не было\n\n\n')

# Функции отладки закоментированы
# Python 3.8
# ~~~> ЗДЕСЬ МОГЛА БЫТЬ ВАША РЕКЛАМА <~~~
