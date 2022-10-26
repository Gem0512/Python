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


def check(n):
    s = n[::-1]
    if(n != s):
        if check_prime_number(int(n)) == 1 and check_prime_number(int(s)) == 1:
            return True
        else:
            return False
    else:
        return False


for i in range(int(input())):
    n = int(input())
    f = [0]*n
    for j in range(1, int(n), 2):
        j = str(j)
        if check(j) and int(j[::-1]) < n and f[int(j)] == 0 and f[int(j[::-1])] == 0:
            print(j+" " + j[::-1], end=' ')
            f[int(j)] = 1
            f[int(j[::-1])] = 1

    print()
