arr =[ [0 for i in range(101)] for _ in range(101)]
n = int(input())

cnt = 0
for i in range(n):
    a, b = map(int, input().split())
    b -= 99
    for j in range(b, b - 10):
        for k in range(a, a+10):
            arr[j][k] = 1

for i in range(1, 101):
    for j in range(1, 101):
        if arr[i][j] == 1:
            cnt += 1

print(cnt)