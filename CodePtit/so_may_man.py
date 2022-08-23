t = int(input())

while t > 0:
    s = str(input())
    ok = "YES"
    for i in s:
        if i != '4' and i != '7':
            ok = "NO"
    print(ok)
    t = t-1
