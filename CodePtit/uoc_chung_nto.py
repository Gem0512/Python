import math


def tong(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = int(n/10)

    return sum


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
    a, b = input().split()
    a = int(a)
    b = int(b)
    # print(math.gcd(a, b))
    # print(tong(math.gcd(a, b)))
    if check_prime_number(tong(math.gcd(a, b))) == 1:
        print("YES")
    else:
        print("NO")
