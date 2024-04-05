n = int(input())
arr = list(map(int, input().split()))

arr.sort()
ans = 0
# [1,2,3,4]
for i in range(len(arr)):
    sum = 0
    for j in range(i+1):
        sum += arr[j]
    ans += sum

print(ans)