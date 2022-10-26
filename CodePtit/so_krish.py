def gthua(n):
    s = 1
    for i in range(1, n+1):
        s = s*i
    return s


for i in range(int(input())):
    n = str(input())
    sum = 0
    # print(gthua(int(n)))
    for j in n:
        j = int(j)
        sum += gthua(j)
        if sum > int(n):
            break
    if(sum == int(n)):
        print("Yes")
    else:
        print("No")
