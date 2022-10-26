n = int(input())
a = [int(i) for i in input().split()]
sum = 0
for i in a:
    sum += i
# print(sum)
# s = float(sum/n)
# print(s)
miz = 99999
l = 0
for i in a:
    l = l+i
    if sum-l-l < miz:
        miz = sum-l-l
        k = i

t = 0
for i in a:
    if i != k:
        t += abs(i-k)

print(t, k)
