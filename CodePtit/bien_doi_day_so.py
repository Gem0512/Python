while True:
    arr = [int(i) for i in input().split()]

    if arr[0] == 0 and (arr[0] == arr[1] and arr[1] == arr[2] and arr[2] == arr[3]):
        break

    count = 0
    while (arr[0] == arr[1] and arr[1] == arr[2] and arr[2] == arr[3]) == False:
        count = count + 1
        tmp = arr[0]
        arr[0] = abs(arr[0] - arr[1])
        arr[1] = abs(arr[1] - arr[2])
        arr[2] = abs(arr[2] - arr[3])
        arr[3] = abs(arr[3] - tmp)
    print(count)
