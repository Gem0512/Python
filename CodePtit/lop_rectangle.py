import math


class Rectangle:
    def __init__(self, chieudai, chieurong, mausac):
        self.chieurong = chieurong
        self.chieudai = chieudai
        self.mausac = mausac

    def perimeter(self):
        return (self.chieurong + self.chieudai)*2

    def area(self):
        return (self.chieurong*self.chieudai)

    def color(self):
        return self.mausac.lower().capitalize()


arr = input().split()
r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
if int(arr[0]) <= 0 or int(arr[1]) <= 0:
    print("INVALID")
else:
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
