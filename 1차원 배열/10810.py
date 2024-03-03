n, m = map(int, input().split())
a = [0]*101
for item in range(m):
    i, j, k = map(int, input().split())
    for c in range(i, j+1):
        a[c] = k

for i in range(1, n+1):
    print(a[i], end=' ')

