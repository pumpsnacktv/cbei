import sys

n = int(input())
arr = []

for i in range(n):
    arr.append(int(sys.stdin.readline()))

arr = sorted(arr)

for i in arr:
    print(i)