def tn(s):
    s1 = str(s)
    s2 = s1[::-1]
    if s1 == s2:
        return 1
    else:
        return 0


def check(s):
    s = str(s)
    for i in s:
        if i != 0 and i != 2 and i != 4 and i != 6 and i != 8:
            return 0
        else:
            return 1


def check1(s):
    s = str(s)
    if len(s) % 2 == 0:
        return 1
    else:
        return 0


for i in range(int(input())):
    for j in range(int(input())):
        if tn(j) == 1 and check(j) == 1 and check1(j) == 1:
            print(j, end=' ')
    print()
