for i in range(int(input())):
    s = str(input())
    ok = "YES"
    for i in range(0, len(s)-1):
        if s[i] > s[i+1]:
            ok = "NO"
            break
    print(ok)
