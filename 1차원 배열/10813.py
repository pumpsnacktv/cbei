a = [0]
for i in range(1,101):
    a.append(i)
n, m = map(int, input().split())
for i in range(1, m+1):
    j, k = map(int, input().split())
    a[k], a[j] = a[j], a[k]
    # temp = a[k]
    # a[k] = a[j]
    # a[j] = temp

for i in range(1, n+1):
    print(a[i], end=' ')

