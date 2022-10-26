from math import gcd


a, b = input().split()
a = int(a)
b = int(b)
dem = 0
for i in range(10**(b-1), 10**b):
    if gcd(a, i) == 1:
        print(i, end=' ')
        dem = dem+1
        if dem == 10:
            print()
            dem = 0
