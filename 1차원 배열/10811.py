n, m = map(int, input().split())
a = [0]
for i in range(1, n+1):
    a.append(i)

for item in range(m):
    i, j = map(int, input().split())
    while i < j: 
        temp = a[i]
        a[i] = a[j]
        a[j] = temp
        i += 1
        j -= 1

for i in range(1, n+1):
    print(a[i], end=' ')
