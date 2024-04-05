n = int(input())
arr = list(map(int, input().split()))
m = int(input())

ans = 0
left = 1
right = max(arr)
while left <= right:
    mid = (left+right)//2  # mid: 상한액 
    sum = 0
    for i in arr:
        if i < mid:
            sum += i
        else:
            sum += mid
    if sum <= m:
        ans = max(ans, mid)
        left = mid+1
    else:
        right = mid-1

print(ans)

