for i in range(int(input())):
    s1 = list(input())
    s2 = list(input())
    s1.sort()
    s2.sort()
    print("Test "+str(i+1)+": ", end='')
    if len(s1) == len(s2):
        ok = "YES"
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                ok = "NO"
                break
        print(ok)
