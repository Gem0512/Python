def check_prime_number(n):
    str1 = str(n)
    str2 = str1[::-1]
    if (str1 == str2):
        return True
    else:
        return False


n, m = input().split()
n = int(n)
m = int(m)
a = []

for i in range(n):
    a.append([int(i) for i in input().split()])
maz = 0
ok = 0
for i in range(0, n):
    for j in range(0, m):
        if check_prime_number(a[i][j]):
            if maz < a[i][j]:
                maz = a[i][j]
            ok = 1
if ok == 0 or len(str(maz)) < 2:
    print("NOT FOUND")
else:
    print(maz)
    for i in range(0, n):
        for j in range(0, m):
            if a[i][j] == maz:
                print("Vi tri "+"["+str(i)+"]["+str(j)+"]")
