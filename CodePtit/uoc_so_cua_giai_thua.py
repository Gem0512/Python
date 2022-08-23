def check(num):
    string = str(num)
    res = 1
    for i in string:
        res += int(i)
    return res


for i in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    for i in range(0, n-1):
        for j in range(i+1, n):
            if(check(a[j]) < check(a[i])) or (check(a[j]) == check(a[i]) and a[j] < a[i]):
                a[i], a[j] = a[j], a[i]
    for i in a:
        print(i, end=" ")
    print()
