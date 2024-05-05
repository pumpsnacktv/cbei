n, k = map(int, input().split())

_max = 0
for i in range(1, k+1):
    temp = n*i
    rev = 0
    while temp != 0:
        rev *= 10
        rev += (temp % 10)
        temp //= 10
    
    if _max < rev:
        _max = rev

print(_max)