import math


def ob(tu, mau):
    return PhanSo(tu, mau)


class PhanSo:
    def __init__(s, x, y):
        s.x = x
        s.y = y

    def toigian(s):
        m = math.gcd(s.x, s.y)
        s.x = s.x/m
        s.y = s.y/m

    def add(s, PhanSo):
        mau = s.y*PhanSo.y
        tu = s.x*PhanSo.y+s.y*PhanSo.x
        return ob(tu, mau)

    def __str__(s):
        return"{}/{}".format(int(s.x), int(s.y))


m, n, p, q = map(int, input().split())
phanso1 = PhanSo(m, n)
phanso2 = PhanSo(p, q)
phanso = phanso1.add(phanso2)
phanso.toigian()
print(phanso)
