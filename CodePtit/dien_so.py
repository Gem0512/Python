for i in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    l = min(a)
    r = max(a)
    dem = 0
    for i in range(l, r):
        if i not in a:
            dem += 1
    print(dem)
