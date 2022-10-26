for i in range(int(input())):
    s = str(input())
    sum = 0
    for j in s:
        sum += int(j)
    sum = str(sum)
    x = "".join(reversed(sum))
    if x == sum and len(sum) > 1:
        print("YES")
    else:
        print("NO")
