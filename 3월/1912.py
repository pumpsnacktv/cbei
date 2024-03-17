import sys
n = int(input())

arr = list(map(int, sys.stdin.readline().split()))
# arr[i]: i번째의 수까지의 연속합   

for i in range(1, n):
    if arr[i] < arr[i-1]+arr[i]:
        arr[i] = arr[i-1]+arr[i]

print(max(arr))


