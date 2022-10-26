import math


for i in range(int(input())):
    a = input().split()
    res = 0
    sum = 0
    for j in range(len(a)):
        sum += int(a[j])
    for j in range(len(a)):
        if abs(int(a[j])-int(a[j+1])) != 2:
            res = 1
            break
    if sum % 10 != 0 and res == 1:
        print("NO")
    else:
        print("YES")
