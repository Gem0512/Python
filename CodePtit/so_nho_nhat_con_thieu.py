n = int(input())
a = [int(i) for i in input().split()]
ok = 1
for i in range(1, n+1):
    if i in a:
        continue
    else:
        print(i)
        ok = 0
        break
if ok == 1:
    print(n+1)
