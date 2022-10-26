n = int(input())
a = []
while len(a) < n:
    b = [int(i) for i in input().split()]
    a.append(b)
maz = max(a)
a = a.sort()
for i in range(1, maz):
    if i not in a:
        print(i)
