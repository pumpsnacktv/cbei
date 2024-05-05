a = list(map(int, input().split()))

cnt = min(a)
while True:
    r = 0
    for i in a:
        if cnt % i == 0:
            r += 1
    
    if r >= 3:
        print(cnt)
        break
    cnt += 1