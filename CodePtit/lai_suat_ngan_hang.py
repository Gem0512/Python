for i in range(int(input())):
    n, x, m = input().split()
    dem = 0
    while float(n) < float(m):
        n = float(n)*(float(x)/100)+float(n)
        dem = dem+1
    print(dem)
