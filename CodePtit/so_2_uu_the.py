import queue


def xly(s):
    dem = 0
    for i in s:
        if i == '2':
            dem += 1
    return dem > len(s)//2


a = []
q1 = queue.Queue()
q1.put('1')
q1.put('2')
a.append('2')
while True:
    x = q1.get()
    # print(x)
    if len(x) >= 9:
        break
    q1.put(x+"0")
    q1.put(x+"1")
    q1.put(x+"2")
    if xly(x+"0"):
        a.append(x+"0")
    if xly(x+"1"):
        a.append(x+"1")
    if xly(x+"2"):
        a.append(x+"2")
n = int(input())
while n > 0:
    n -= 1
    m = int(input())
    for i in range(m):
        print(a[i], end=' ')
    print()
