for i in range(int(input())):
    s = str(input())

    if s[len(s)-2:] == "86":
        print("YES")
    else:
        print("NO")
