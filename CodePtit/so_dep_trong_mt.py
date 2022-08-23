n, m = input().split()
n = int(n)
m = int(m)
a = []

for i in range(n):
    a.append([int(i) for i in input().split()])
miz = 10000
maz = 0
for i in range(0, n):
    for j in range(0, m):
        if a[i][j] < miz:
            miz = a[i][j]
        if a[i][j] > maz:
            maz = a[i][j]
l = maz-miz
ok = 0
for i in range(0, n):
    for j in range(0, m):
        if a[i][j] == l:
            h = a[i][j]
            ok = 1
if ok == 0:
    print("NOT FOUND")
else:
    print(l)
    for i in range(0, n):
        for j in range(0, m):
            if a[i][j] == h:
                print("Vi tri "+"["+str(i)+"]["+str(j)+"]")
