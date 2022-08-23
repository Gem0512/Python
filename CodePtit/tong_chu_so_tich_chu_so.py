for i in range(int(input())):
    s = str(input())
    sum = 0
    t = 1
    dem = 0
    for j in range(len(s)):
        if j % 2 != 0:
            sum += int(s[j])
        else:
            if s[j] != '0':
                t = t*int(s[j])
                dem += 1
    if dem == 0:
        print(0, sum)
    else:
        print(t, sum)
