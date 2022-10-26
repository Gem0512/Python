n, k = input().split()
n = int(n)
k = int(k)
s = input()
a = s.split()
a = set(a)
a = sorted(a)
l = len(a)


def Try(i):
    for j in range(ord(a[i-1])+1, n-k+1):
        a[i] = j
        if i == k:
            for k in range(1, k):
                s = chr(a[i] + -1)
                print(s)
        else:
            Try(i+1)


Try(1)
