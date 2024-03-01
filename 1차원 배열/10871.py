n, x = map(int, input().split())
arr = map(int, input().split())


for item in arr:
    if item < x:
        print(item, end=' ')