for i in range(int(input())):
    s = str(input())
    a = len(s)

    if s[:2] == s[a-2:]:
        print("YES")
    else:
        print("NO")
