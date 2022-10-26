import math


class HoaDon:
    def __init__(self, id, ten, old, new):
        self.id = id
        self.ten = ten
        self.old = old
        self.new = new
        self.khoangcach = new-old

    def tinhTien(self):
        sum = 0
        if self.khoangcach <= 50:
            self.tongtien = self.khoangcach*100*1.02
        if 50 < self.khoangcach <= 100:
            self.tongtien = (50*100+(self.khoangcach-50)*150)*1.03
        if self.khoangcach > 100:
            self.tongtien = (50*100+50*150+(self.khoangcach-100)*200)*1.05

    def __str__(self):
        if self.id < 10:
            return "KH0{} {} {}".format(self.id, self.ten, math.ceil(self.tongtien))
        else:
            return "KH{} {} {}".format(self.id, self.ten, math.ceil(self.tongtien))


data = []
for i in range(int(input())):
    hd = HoaDon(i+1, input(), int(input()), int(input()))
    hd.tinhTien()
    data.append(hd)
data = sorted(data, key=lambda x: x.tongtien, reverse=True)
for i in data:
    print(i)
