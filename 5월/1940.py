n = int(input())
m = int(input())

arr = list(map(int, input().split()))
arr.sort()
cnt = 0
start = 0
end = n-1

while end > start:
    if arr[start]+arr[end] == m:
        cnt += 1
        end -= 1
        start += 1
    elif arr[start]+arr[end] > m:
        end -= 1
    else:
        start += 1

print(cnt)


# n = int(input())
# m = int(input())
# check = [0]*10000001
# arr = list(map(int, input().split()))
# cnt = 0

# for i in arr:
#     check[i] = 1

# for i in arr:
#     if check[m - i] == 1:
#         cnt += 1

# print(cnt//2)