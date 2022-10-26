for i in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    a.sort()
    b.sort()
    ok = 1
    for j in range(n):
        if a[j] > b[j]:
            ok = 0
            break
    if ok == 1:
        print("YES")
    else:
        print("NO")
