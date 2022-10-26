def check_prime_number(n):
    flag = 1
    if (n < 2):
        flag = 0
        return flag
    for p in range(2, n):
        if n % p == 0:
            flag = 0
            break
    return flag


for i in range(int(input())):
    n = int(input())
    if check_prime_number(n) == 1:
        n = str(n)
        print("1 * "+n+"^1")
    else:
        print("1 * ", end='')
        for j in range(2, n):
            dem = 0

            while(n % j == 0):
                dem += 1
                n /= j
            if(dem != 0):

                print(j, end='')
                if(dem >= 1):
                    dem = str(dem)
                    print("^" + dem, end='')
                if(n > j):
                    print(" * ", end='')
        print()
