s = input()
s1 = input()

a = float(input())
b = float(input())
c = float(input())
print(s, end=' ')

if (s1[2] != '/'):
    s1 = "0"+s1
if (s1[5] != '/'):
    f = s1[0, 3]
    e = s1[3, s1.length()]
    s1 = f+"0"+e
print(s1, end=' ')
sum = a+b+c
print("{:.1f}".format(sum))
