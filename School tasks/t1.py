x = m = n = 0
x = int(input('Enter a number: '))
while x > 0:
    if n < x % 10:
        n = x % 10
    m += 1
    x = x // 10
print(m, n)