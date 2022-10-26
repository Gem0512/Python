
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


# m, n = input().split()
# m = int(m)
# n = int(n)
# a = []

# for i in range(0, m):
#     a.append([])
#     for j in range(0, n):
#         x = input().split()
#         a[i].append(x)

# for i in range(0, m):
#     for j in range(0, n):
#         if check_prime_number(a[i][j]) == 1:
#             print(a[i][j], end='')
#     print()


m, n = input().split()
m = int(m)
n = int(n)
danhSach2Chieu = []
for i in range(m):
    hang = input()
    danhSach2Chieu.append(hang)

for hang in danhSach2Chieu:
    hang = hang.split()
    for j in hang:
        j = int(j)
        if check_prime_number(j) == 1:
            print(1, sep=' ', end=' ')
        else:
            print(0, sep=' ', end=' ')
    print()
