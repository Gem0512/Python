for i in range(int(input())):
    s = str(input())
    x = list(s)

    # x = set(x)
    ok = 1
    for i in range(len(x)-2):
        if x[i] != x[i+2]:
            ok = 0
            break
    if ok == 1 and len(set(x)) == 2:
        print("YES")
    else:
        print("NO")
