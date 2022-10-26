s1 = input().lower()
s2 = input().lower()
a = set(s1.split())
b = set(s2.split())

u = a.union(b)
u = sorted(u)
for i in u:
    print(i, end=' ')
print()
v = a & b
v = sorted(v)
for i in v:
    print(i, end=' ')
