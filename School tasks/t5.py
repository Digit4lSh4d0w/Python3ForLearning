num = int(input('Enter a number: '))
ans = []

def to_three(num, ans):
    if num < 3:
        ans.append(str(num))
    else:
        ans.append(str(num%3))
        to_three(num//3, ans)
        return ans[::-1]

print(''.join(to_three(num, ans)))

# 1010101 -> 1220022121011
# 1091091 -> 2001102200210
# 1683721 -> 10011112122001
# 3762918 -> 21002011202100
# 3820701 -> 21012010000110