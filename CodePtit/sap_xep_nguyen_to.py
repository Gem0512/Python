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
b = []
for i in a:
    if check_prime_number(i) == 1:
        b.append(i)
b = b.sort()
dem = 0
for i in a:
    if check_prime_number(i) == 1:
        print(b[dem], end=' ')
        dem += 1
    else:
        print(i, end=' ')
# for i in b:
#     print(i, end=' ')
