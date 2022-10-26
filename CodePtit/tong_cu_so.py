def tong(n):
    sum = 0
    if n[0] == '-':
        sum = (ord('-') - ord('0'))
        for j in range(1, len(n)):
            sum += int(n[j])
    else:
        for j in n:
            sum += int(j)
    return sum


n = input()
dem = 0
while len(n) > 1:
    dem += 1
    n = str(tong(n))

print(dem)

# for j in range(1, len(n)):
#     print(n[j])
