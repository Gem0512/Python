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
    s = str(input())
    l = len(s)
    res = "YES"
    dem = 0
    for j in s:
        if check_prime_number(int(j)) == 1:
            dem += 1
    if check_prime_number(l) == 0 or dem <= l-dem:
        res = "NO"
    print(res)
