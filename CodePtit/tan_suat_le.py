for i in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().strip().split()]
    f = {}
    for i in a:
        if i in f:
            f[i] += 1
        else:
            f[i] = 1
    for i in a:
        if f[i] % 2 != 0:
            print(i)
            break
