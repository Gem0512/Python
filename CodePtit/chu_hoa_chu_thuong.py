s = str(input())
l = len(s)
dem1 = 0
dem2 = 0
for i in s:
    if i.islower():
        dem1 = dem1+1
if dem1 >= l-dem1:
    print(s.lower())
else:
    print(s.upper())
