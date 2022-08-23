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
    sum = 0
    for j in range(0, len(s)):

        if j % 2 == 0:
            if int(s[j]) % 2 != 0:
                ok = 0
                break
        else:
            if int(s[j]) % 2 == 0:
                ok = 0
                break
        sum += int(s[j])
    if ok == 0 or check_prime_number(sum) == 0:
        print("NO")
    else:
        print("YES")
