n, m = map(int, input().split())
arr = list(map(int, input().split()))

ans = -1
for i in range(0, n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if arr[i]+arr[j]+arr[k] > m:
                continue
            elif arr[i]+arr[j]+arr[k] > ans:
                ans = arr[i]+arr[j]+arr[k]

print(ans)
