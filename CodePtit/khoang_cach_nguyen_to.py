from math import sqrt


def prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True


n, x = input().split()
n = int(n)
x = int(x)
print(x, end=" ")
i = 0
cc = False
while True:
    for j in range(2, 1000005):
        if prime(j):
            x = j+x
            print(x, end=" ")
            i += 1
            if i == n:
                cc = True
                break
    if cc:
        break
