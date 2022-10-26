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
b = dict.fromkeys(a)
s = 0
for i in b:
    s = s+i
ok = 0

sum = 0
k = 0
for i in b:
    sum = sum+i
    if check_prime_number(sum) == 1 and check_prime_number(s-sum) == 1:
        ok = 1
        print(k)
        break
    k += 1
    # print(sum)

if ok == 0:
    print("NOT FOUND")
