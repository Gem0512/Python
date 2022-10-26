n, m = input().split()
n = int(n)
m = int(m)
a = []

for i in range(n):
    a.append([int(i) for i in input().split()])

if n > m:
    dem = 0
    k = n-m
    for i in range(n):
        if (i-1) % 2 == 0 and k != dem:
            dem += 1
            for j in range(m):
                print(a[i][j], end=' ')
            print()
        elif k == dem:
            for j in range(m):
                print(a[i][j], end=' ')
            print()
else:

    k = m-n
    for i in range(n):
        dem = -1
        for j in range(m):
            if (j-1) % 2 != 0:
                dem += 1
                if k != dem:
                    print(a[i][j], end=' ')
            if k == dem:
                print(a[i][j], end=' ')
        print()
