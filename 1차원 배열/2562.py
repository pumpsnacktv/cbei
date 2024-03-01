max_ = -1000001
ans = 0
pos = 0

for i in range(9):
    temp = int(input())
    if temp > max_:
        pos = i+1
        max_ = temp

print(max_)
print(pos)