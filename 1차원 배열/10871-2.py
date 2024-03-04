n, x = list(map(int, input().split()))
arr = list(map(int, input().split()))


for item in arr:
    if item < x:
        print(item, end=' ')