import sys
n = int(input())

arr = list(map(int, sys.stdin.readline().split()))
dp = [0]

for i in range(1, n):
    if arr[i] < dp[i-1]+arr[i]:
        dp.append(dp[i-1]+arr[i])
    else:
        dp.append(arr[i])

print(max(dp))

