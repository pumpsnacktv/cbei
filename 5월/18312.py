n, k = map(int, input().split())
cnt = 0

for h in range(0, n+1):
    for m in range(0, 60):
        for s in range(0, 60):
            if h % 10 == k or h // 10 == k:
                cnt += 1
            elif m % 10 == k or m // 10 == k:
                cnt += 1
            elif s % 10 == k or s // 10 == k:
                cnt += 1
print(cnt)            