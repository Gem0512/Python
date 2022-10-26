class Maxtric:
    def __init__(self, x, y, a):
        self.x = x
        self.y = y
        self.a = a

    def tich(self):
        for i in range(self.x):
            for j in range(self.x):
                n = 0
                for k in range(self.y):
                    n += (self.a[i][k]*self.a[j][k])
                print(n, end=' ')
            print()


for i in range(int(input())):
    x, y = map(int, input().split())
    a = []
    for j in range(x):
        a.append([int(i) for i in input().split()])
    mt = Maxtric(x, y, a)
    mt.tich()
