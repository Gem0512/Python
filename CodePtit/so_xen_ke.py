for i in range(int(input())):
    s = str(input())
    ok = 1
    for j in range(1, len(s)-2):
        if s[i] != s[i+2]:
            ok = 0
    if len(s) % 2 == 0 or s[0] == s[1] or ok == 0:
        print("NO")
    else:
        print("YES")
