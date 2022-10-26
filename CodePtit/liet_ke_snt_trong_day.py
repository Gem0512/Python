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


n = int(input())
a = [int(i) for i in input().split()]
f = {}
for i in a:
    if i in f:
        f[i] += 1
    else:
        f[i] = 1

s = dict.fromkeys(a)
for i in s:
    i = int(i)
    if check_prime_number(i) == 1:
        print(i, f[i])
        # a.pop()
        print()
