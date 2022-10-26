import math


for i in range(int(input())):
    s = str(input())
    x = "".join(reversed(s))
    ok = "YES"
    for j in range(len(s)):
        if abs(ord(s[j])-ord(s[j-1])) != abs(ord(x[j])-ord(x[j-1])):
            ok = "NO"
            break
    print(ok)
