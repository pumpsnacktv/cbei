_max = -50
cur = 0

for i in range(4):
    b,a = map(int, input().split())
    cur -= b
    cur += a
    if cur > _max:
        _max = cur
print(_max)