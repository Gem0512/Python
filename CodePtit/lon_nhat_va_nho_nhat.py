while 1:
    n = int(input())
    if n == 0:
        break
    maz = 0
    miz = 1e9
    for i in range(n):
        x = int(input())
        if x != miz and x != maz:
            if x > maz:
                maz = x
            if x < miz:
                miz = x
    if miz == maz:
        print("BANG NHAU")
    else:
        print(miz, maz)
