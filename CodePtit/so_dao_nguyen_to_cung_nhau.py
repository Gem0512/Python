from math import gcd


for i in range(int(input())):
    s = str(input())
    x = "".join(reversed(s))
    if gcd(int(s), int(x)) == 1:
        print("YES")
    else:
        print("NO")
