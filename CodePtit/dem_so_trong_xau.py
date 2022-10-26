for i in range(int(input())):
    s = str(input())
    x = str(input())
    l = len(x)
    dem = 0
    j = 0
    while j <= len(s)-l:
        s1 = str(s[j:(j+l)])
        if s1 == x:
            dem += 1
            j = j+l
        else:
            j += 1

    print(dem)

# s = str(input())
# x = str(input())
# s1 = str(s[0:3])
# if s1 == x:
#     print("=====")
# print(str(s[0:3]))
