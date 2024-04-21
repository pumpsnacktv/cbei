pos = 0
_max = -99
for i in range(9):
    temp = int(input())
    if temp > _max:
        _max = temp
        pos = i+1

print(_max)
print(pos)