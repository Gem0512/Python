for i in range(int(input())):
    p, q = input().split()
    p = int(p)
    q = int(q)
    try:
        x1, x2 = input().split()
        maz = str(max(q, p))
        miz = str(min(p, q))
    except:
        x1 = str(input())
        x2 = str(input())
    maz = str(max(q, p))
    miz = str(min(p, q))
    x1 = x1.replace(maz, miz)
    x2 = x2.replace(maz, miz)
    print(int(x1)+int(x2), end=" ")
    x1 = x1.replace(miz, maz)
    x2 = x2.replace(miz, maz)
    print(int(x1)+int(x2))
