dell = int(input('Число кратное: '))
num = 1                 # Первое число
while True:
    sum = 0             # Сумма цифр числа
    sumS = 0            # Сумма цифр числа + 2
    string = []         # Число по частям
    stringS = []        # Число + 2 по частям
    string = list(str(num))
    for ciph in string:
        sum += int(ciph)
    if sum % dell == 0:
        numS = num + 2
        stringS = list(str(numS))
        for ciphS in stringS:
            sumS += int(ciphS)
        if sumS % dell == 0:
            print('Succes %s'%(num))
    num += 1
