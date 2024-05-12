import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
rarr = [0 for i in range(sum(arr)+1)]

def d(i, s):
    global n, arr
    if i == n:
        if s > 0:
            rarr[s] = 1
        return
    a = arr[i]
    d(i+1, s-a)
    d(i+1, s+a)
    d(i+1, s)

d(0, 0)
res = sum(arr)
for i in range(sum(arr)+1):
    res -= rarr[i]

print(res)