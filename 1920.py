import sys
from bisect import bisect_left, bisect_right

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
arr = sorted(arr)
m = int(input())
q = list(map(int, sys.stdin.readline().split()))

for i in q:
    if bisect_left(arr, i) == bisect_right(arr, i):
        print(0)
    else:
        print(1)