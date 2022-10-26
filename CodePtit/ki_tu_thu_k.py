

for i in range(int(input())):
    n, k = input().split()
    n = int(n)
    k = int(k)
    n = n-1
    while n >= 0:
        h = 2**n
        if k % h == 0:
            x = ord('A')+n
            x = chr(x)
            print(x)
            break
        n = n-1
