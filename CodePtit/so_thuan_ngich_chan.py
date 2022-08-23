
def check(s):
    ok = 1
    s = str(s)
    for j in s:
        if int(j) % 2 != 0:
            ok = 0
            break
    x = "".join(reversed(s))
    if ok == 0 or x != s or len(s) % 2 != 0:
        return 0
    else:
        return 1


for i in range(int(input())):
    s = int(input())
    for j in range(s):
        if check(j) == 1:
            print(j, end=' ')
    print()
