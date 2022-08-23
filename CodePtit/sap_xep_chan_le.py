n = int(input())
a = []
while len(a) < n:
    a.extend(list(map(int, input().strip().split())))
chan = []
le = []

for i in a:
    if i % 2 == 1:
        le.append(i)
    else:
        chan.append(i)
chan.sort()
le.sort(reverse=True)
m1 = 0
m2 = 0
for i in a:
    if i % 2 == 1:
        print(le[m1], end=" ")
        m1 += 1
    else:
        print(chan[m2], end=" ")
        m2 += 1
