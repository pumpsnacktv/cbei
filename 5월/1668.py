n = int(input())
arr = []
_max = 0
ans1, ans2 = 0, 0
for i in range(n):
    temp = int(input())
    arr.append(temp)
    if temp > _max:
        ans1 += 1
        _max = temp
_max = 0
for i in range(n-1, -1, -1):
    if arr[i] > _max:
        ans2 += 1
        _max = arr[i]

print(ans1)
print(ans2)