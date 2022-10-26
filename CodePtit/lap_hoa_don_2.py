import datetime
import math


class HoaDon:
    def __init__(self, name, phong, start, end, chiphi, id):
        self.name = name
        self.phong = phong
        self.start = start
        self.end = end
        self.chiphi = chiphi
        self.id = 'KH%02d' % id
        self.day = 0
        self.tongtien = 0

    def tinhNgay(self):
        if self.start == self.end:
            self.day = 1
            return
        time_in = datetime.datetime.strptime(self.start, '%d/%m/%Y')
        time_out = datetime.datetime.strptime(self.end, '%d/%m/%Y')
        dis = str(time_out-time_in)
        dis = [i for i in dis.split(" ")]
        self.day = int(dis[0])+1

    def tinhTien(self):
        if self.phong[0] == '1':
            self.tongtien = self.day*25+self.chiphi
        if self.phong[0] == '2':
            self.tongtien = self.day*34+self.chiphi
        if self.phong[0] == '3':
            self.tongtien = self.day*50+self.chiphi
        if self.phong[0] == '4':
            self.tongtien = self.day*80+self.chiphi

    def __str__(self):
        return "{} {} {} {} {}".format(self.id, self.name, self.phong, self.day, self.tongtien)


data = []
for i in range(int(input())):
    name = input().strip()
    phong = input()
    start = input().strip()
    end = input().strip()
    chiphi = int(input().strip())
    data.append(HoaDon(name, phong, start, end, chiphi, i+1))
for i in data:
    i.tinhNgay()
    i.tinhTien()
data = sorted(data, key=lambda x: x.tongtien, reverse=True)
for i in data:
    print(i)
