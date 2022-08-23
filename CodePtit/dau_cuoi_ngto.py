
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
    x = int(s[:3])
    y = int(s[len(s)-3:])
    if check_prime_number(x) == 1 and check_prime_number(y) == 1:
        print("YES")
    else:
        print("NO")
