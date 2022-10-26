def doicho(s):
    l = len(s)
    index = -1
    for i in range(l-2, 0, -1):
        if s[i] > s[i+1]:
            index = i
            break
    k = -1
    for i in range(l-1, index, -1):
        if s[i] < s[index]:
            if k == -1:
                k = i
        else:
            if s[i] >= s[k]:
                k = i
    if index == -1:
        return "-1"
    if k != -1:
        a = s[index]
        s[index] = s[k]
        s[k] = a
        return s
    return "-1"


for i in range(int(input())):
    a = str(input())
    b = doicho(a)
    if b[0] == '0':
        print(-1)
    else:
        print(b)
