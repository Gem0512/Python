for i in range(int(input())):
    s = str(input())
    sum = 0
    for j in s:
        sum += int(j)
    if sum % 3 == 0:
        print("YES")
    else:
        print("NO")
