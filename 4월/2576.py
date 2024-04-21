arr = []
_sum = 0
for i in range(7):
    temp = int(input())
    if temp % 2 == 1:
        _sum += temp
        arr.append(temp)
if _sum == 0:
    print(-1)
    exit()
print(_sum)
print(min(arr))