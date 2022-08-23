for i in range(int(input())):
    f = {}
    n = int(input())
    a = [int(i) for i in input().split()]
    for i in a:
        if i in f:
            f[i] += 1
        else:
            f[i] = 1
    res = 0
    for i in f:
        if f[i] >= int(n/2)+1:
            print(i)
            res = 1
            break
    if res == 0:
        print("NO")
