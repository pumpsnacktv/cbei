max_ = -1000001
ans = 0
pos = 0

temp = list(map(int, input().split()))

for i in range(9):
    if temp[i] > max_:
        pos = i+1
        max_ = temp[i]

print(max(temp))
print(pos)