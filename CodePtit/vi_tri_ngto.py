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
    ok = 1
    for j in range(0, len(s)):
        if check_prime_number(int(j)) == 1:
            if check_prime_number(int(s[j])) == 0:
                ok = 0
                break
        else:
            if check_prime_number(int(s[j])) == 1:
                ok = 0
                break
    if ok == 1:
        print("YES")
    else:
        print("NO")
