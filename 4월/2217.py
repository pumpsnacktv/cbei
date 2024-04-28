n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)
_max = 0
for i in range(n):
    if arr[i]*(i+1) > _max:
        _max = arr[i]*(i+1)

print(_max)
