n = int(input())
a = [float(i) for i in input().split()]
dem = 0
sum = 0
for i in a:
    if i == max(a) or i == min(a):
        dem += 1
    else:
        sum += i
k = n-dem
print("{:.2f}".format(sum/k))
