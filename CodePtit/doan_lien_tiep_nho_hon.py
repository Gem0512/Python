for k in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]

    for i in range(n):
        dem = 0
        for j in range(0, i+1):
            if a[i] >= a[i-j]:
                dem += 1
            else:
                break
        print(dem, end=' ')
    print()
