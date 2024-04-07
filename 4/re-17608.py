import sys
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    temp = int(sys.stdin.readline())
    arr.append(temp)
cnt = 0
_max = 0

for i in range(n-1, -1, -1):
    if _max < arr[i]:
        cnt += 1
        _max = arr[i]

print(cnt)