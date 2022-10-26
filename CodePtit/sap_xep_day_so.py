for i in range(int(input())):
    n, k = input().split()
    n = int(n)
    k = int(k)
    a = [int(j) for j in input().split()]
    maz = max(a)
    for j in range(n):
        if a[j] == maz:
            index = j
            break
    a.insert(index, k)
    for j in a:
        if j < 0:
            print(j, end=" ")
    for j in a:
        if j >= 0:
            print(j, end=' ')
    print()
