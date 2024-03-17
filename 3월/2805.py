import sys

n, m = map(int, input().split())
arr = list(map(int, sys.stdin.readline().split()))

l, r = 0, 1000000000
result = 0
while l <= r:
    mid = (l+r) // 2
    print(l, r, mid, result)
    s = 0
    for i in arr:
        s += max(i-mid, 0)
    if s >= m:
        l = mid+1
        result = max(result, mid)
    else:
        r = mid-1
print(result)