for i in range(int(input())):
    s = str(input())
    dem = 1
    l = len(s)
    for i in range(0, l-1):
        if s[i] == s[i+1]:
            dem += 1
        else:
            print(dem, s[i], sep='', end='')
            dem = 1
    print(dem, s[l-1], sep='', end='')
    print()
