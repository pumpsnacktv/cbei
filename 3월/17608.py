import sys
n = int(input())
arr = []
for _ in range(n):
    temp = int(sys.stdin.readline())
    arr.append(temp)
cnt = 0
_max = 0
for i in range(n-1, -1, -1):
    if arr[i] > _max:
        cnt += 1
        _max = arr[i]

print(cnt)
