import sys
n = int(input())
arr = []
for _ in range(n):
    a, b = map(int,sys.stdin.readline().split())
    arr.append((a,b))

arr.sort()
for i in range(n):
    print(i[0], i[1])