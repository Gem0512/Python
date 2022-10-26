s = str(input())
k = int(input())
a = []
f = [0]*1000
for i in range(0, len(s), 2):
    x = s[i:(i+2)]
    if len(x) == 2:
        if f[int(x)] == 0:
            a.append(x)
            f[int(x)] = 1
        else:
            f[int(x)] += 1
a = dict.fromkeys(a)
a = sorted(a)
ok = 0
for i in a:
    if f[int(i)] >= k:
        print(i, f[int(i)])
        ok = 1
if ok == 0:
    print("NOT FOUND")
