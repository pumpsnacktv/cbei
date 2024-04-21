n = int(input())
cnt = 0
arr = list(map(int,input().split()))
for i in arr:
    if n == i:
        cnt += 1
print(cnt)