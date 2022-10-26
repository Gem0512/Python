from calendar import c


def sieve(n):
    ''' sàng nguyên tố [0,n] '''

    danh_dau = [True]*(n+1)  # giả sự lúc đầu đều có thể là snt

    can_n = int(n**0.5)+1  # = floor(sqrt(n))+1

    for i in range(2, can_n+1):  # i= 2->can_n
        if danh_dau[i]:  # i là số nguyên tố

            for j in range(i*i, n+1, i):  # j=i*i, i*i+i , ...,n
                danh_dau[j] = False  # j khong là số nguyên tố

    primes = []
    for i in range(2, n+1):  # i= 2->n
        if danh_dau[i]:
            primes.append(i)  # liệt kê lại số nguyên tố vào mảng mới
    return primes


for i in range(int(input())):
    n = str(input())
    s = n[::-1]
    sum = 0
    ok = 1
    a = sieve(10000000)
    for j in n:
        sum += int(j)
        if int(j) not in a:
            ok = 0
            break
    if ok == 1:
        if (sum in a) and (int(n) in a) and (int(s) in a):
            print("Yes")
        else:
            print("No")
    else:
        print("No")
