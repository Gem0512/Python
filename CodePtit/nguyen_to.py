import math


def check_prime_number(n):
    flag = 1
    if (n < 2):
        flag = 0
        return flag
    for p in range(2, n):
        if n % p == 0:
            flag = 0
            break
    return flag


for i in range(int(input())):
    n = int(input())
    k = 0
    for i in range(n):
        if math.gcd(i, n) == 1:
            k += 1
    if check_prime_number(k) == 1:
        print("YES")
    else:
        print("NO")
