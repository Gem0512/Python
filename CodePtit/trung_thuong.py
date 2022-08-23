for i in range(int(input())):
    f = {}
    n = int(input())
    for j in range(n):
        x = int(input())
        if x in f:
            f[x] += 1
        else:
            f[x] = 1

    res = 1e9
    maz = 1
    for j in f:
        if f[j] > maz:
            maz = f[j]
    for j in f:
        if f[j] == maz:
            res = min(res, int(j))
    print(res)
