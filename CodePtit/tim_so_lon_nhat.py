import re

n = int(input())

while n:

    s = input()
    m = re.findall(r'\d+', s)
    m = [int(i) for i in m]
    print(min(m))
    n -= 1
