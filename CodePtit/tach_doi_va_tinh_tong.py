n = str(input())
while(len(n) > 1):
    n = str(n)
    k = int(len(n)/2)
    s1 = (n[:k])
    s2 = (n[k:])
    p = int(s1)+int(s2)
    n = str(p)
    print(p)
