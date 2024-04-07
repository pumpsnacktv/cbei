import sys
n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
m = int(input())

ans = 0
l = 1
r = max(arr)
while l <= r:
    mid = (l+r)//2
    sum = 0
    for i in arr:
        if i < mid:
            sum += i
        else:
            sum += mid
    