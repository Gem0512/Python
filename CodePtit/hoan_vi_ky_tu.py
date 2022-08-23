def permute(s):
    a = sorted(s)
    n = len(a) - 1
    while True:
        yield ''.join(a)

        for j in range(n-1, -1, -1):
            if a[j] < a[j + 1]:
                break
        else:
            return

        v = a[j]
        for k in range(n, j, -1):
            if v < a[k]:
                break

        a[j], a[k] = a[k], a[j]

        a[j+1:] = a[j+1:][::-1]


s = str(input())
for s in permute(s):
    print(s)
