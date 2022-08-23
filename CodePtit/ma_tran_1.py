n = int(input())
a = []

for i in range(n):
    a.append([int(i) for i in input().split()])
k = int(input())

sum1 = 0
for i in range(0, n-1):
    for j in range(0, n-i-1):
        sum1 += a[i][j]
sum2 = 0
for i in range(1, n):
    for j in range(n-i, n):
        sum2 += a[i][j]
# print(sum1, sum2)

if abs(sum1-sum2) <= k:
    print("YES")
    print(abs(sum1-sum2))
else:
    print("NO")
    print(abs(sum1-sum2))
