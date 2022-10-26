for i in range(int(input())):
    s = str(input())
    t = 1
    for j in s:
        if j != '0':
            t = t*int(j)
    print(t)
