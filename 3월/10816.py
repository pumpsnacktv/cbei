import sys
n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
m = int(input())
arr2 = list(map(int, sys.stdin.readline().split()))
ans = {}  # {key:value, key:value, 10:3, 6:1, 3:2,...........}
for i in arr:
    if i in ans:
        ans[i] += 1
    else:
        ans[i] = 1

for i in arr2:
    if i in ans:
        print(ans[i], end= ' ')
    else:
        print(0, end = ' ')
