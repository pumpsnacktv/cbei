n = int(input())
max_ = -1000001
min_ = 1000001
temp = map(int, input().split())

for i in temp:
    if(i > max_):
        max_ = i
    if(i < min_):
        min_ = i

print(min_, max_)