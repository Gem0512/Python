n, m = map(int, input().split())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
a.sort()
b.sort()
res1 = []
res2 = []
res3 = []
_a = []
_b = []
for i in a:
    if i not in _a:
        _a.append(i)
for i in b:
    if i not in _b:
        _b.append(i)
for i in _a:
    if i in _b:
        res1.append(i)
    else:
        res2.append(i)
for i in _b:
    if i not in _a:
        res3.append(i)
for i in res1:
    print(i, end=" ")
print()
for i in res2:
    print(i, end=" ")
print()
for i in res3:
    print(i, end=" ")
