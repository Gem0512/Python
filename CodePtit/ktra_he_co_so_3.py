for i in range(int(input())):
    s = str(input())
    ok = "YES"
    for j in s:
        # print(j)
        if j != '0' and j != '1' and j != '2':
            ok = "NO"
            break
    print(ok)
