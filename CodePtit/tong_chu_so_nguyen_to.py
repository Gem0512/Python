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
    s = input()
    sum = 0
    for j in s:
        sum += int(j)
    if check_prime_number(sum) == 1:
        print("YES")
    else:
        print("NO")
