def tong(n):
    sum = 0
    n = str(n)
    for i in n:
        sum += int(i)
    return sum


a = [int(i) for i in input().split()]
b = map()
for i in a:
    b[i] = tong(i)
