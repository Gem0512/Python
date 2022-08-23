for i in range(int(input())):
    s = list(input())
    s.sort()
    res = ""
    tong = int(0)
    for j in range(len(s)):
        if s[j] >= '0' and s[j] <= '9':
            tong += int(s[j])
        else:
            res += s[j]
    res += str(tong)
    print(res)
