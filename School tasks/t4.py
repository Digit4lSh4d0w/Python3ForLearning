litNum, bigNum = map(list, input('Enter a numbers: ').split())
numLen = len(litNum)
ans = 0
for i in range(0, len(bigNum) - 1):
    if litNum == bigNum[i:i + numLen]:
        ans = 1
if ans:
    print('True')
else:
    print('False')