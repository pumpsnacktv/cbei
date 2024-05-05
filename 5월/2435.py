n, k = map(int, input().split())

_max = -99999
arr = list(map(int, input().split()))
for i in range(n-k+1):
    temp = 0
    for j in range(i, i+k):
        temp += arr[j]
    if temp > _max:
        _max = temp

print(_max)