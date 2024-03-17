n = int(input())

arr = [0, 1, 2, 3, 5]

if n < 5:
    print(arr[n])
    exit()
else:
    for i in range(5, n+1):
        arr.append(arr[i-2]+arr[i-1])
    print(arr[n]%10007)