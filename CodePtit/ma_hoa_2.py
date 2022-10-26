p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while 1:
    a = input().split()
    k = int(a[0])
    if k == 0:
        break
    s = a[1]

    res = ""
    for i in s:
        res += p[(p.find(i)+k) % 28]
    m = list(res)
    m.reverse()
    for i in m:
        print(i, end='')
    print()
