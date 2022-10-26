import math


class Point:
    def __init__(s, x, y):
        s.x = x
        s.y = y

    def distance(s, p):
        k = math.sqrt((s.x-p.x)**2+(s.y-p.y)**2)
        return "%.4f" % k


def Decimal(n):
    n = float(n)
    return n


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1
