n, m = input().split()
n = int(n)
m = int(m)
a = set([int(i) for i in input().split()])
b = set([int(i) for i in input().split()])

if len(a) == len(b):
    ok = 1
    if a != b:
        print("NO")
    else:
        print("YES")

else:
    print("NO")
