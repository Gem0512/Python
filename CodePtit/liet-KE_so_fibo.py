def fibonacci(n):
    f0 = 0
    f1 = 1
    fn = 1

    if (n < 0):
        return -1
    elif (n == 0 or n == 1):
        return n
    else:
        for i in range(2, n):
            f0 = f1
            f1 = fn
            fn = f0 + f1
        return fn


for i in range(int(input())):
    a, b = input().split()
    a = int(a)
    b = int(b)
    for j in range(a, b+1):
        print(fibonacci(j), end=" ")
