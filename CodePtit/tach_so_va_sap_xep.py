import re
n = int(input())
a = []
while n:
    s = input()
    m = re.findall(r'\d+', s)
    m = [int(i) for i in m]
    n -= 1
    a = a+m
a.sort()
for i in a:
    print(i)
