
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
    if check_prime_number(int(s[len(s)-4:])) == 1:
        print("YES")
    else:
        print("NO")
