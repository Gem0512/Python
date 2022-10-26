for i in range(int(input())):
    a = [str(i) for i in input().split()]
    x = int(a[0])
    y = a[1]
    z = a[2]
    t = a[3]
    if x == 3 or x == 4:
        x = 2.5
    elif x == 5 or x == 6:
        x = 3
    elif x == 7 or x == 8 or x == 9:
        x = 3.5
    elif x == 10 or x == 11 or x == 12:
        x = 4
    elif x == 13 or x == 14 or x == 15:
        x = 4.5
    elif x == 16 or x == 17 or x == 18 or x == 19:
        x = 5
    elif x == 20 or x == 21 or x == 22:
        x = 5.5
    elif x >= 23 and x <= 26:
        x = 6
    elif x >= 26 and x <= 29:
        x = 6.5
    elif x >= 30 and x <= 32:
        x = 7
    elif x >= 33 and x <= 34:
        x = 7.5
    elif x >= 35 and x <= 36:
        x = 8
    elif x >= 37 and x <= 38:
        x = 8.5
    elif x >= 39 and x <= 40:
        x = 9

print(x)
