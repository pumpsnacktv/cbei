arr = []
n, k = map(int, input().split())
cnt = 2
arr.append(1)
for i in range(2, n):
    if n % i == 0:
        cnt += 1
        arr.append(i)
arr.append(n)
if cnt < k:
    print(0)
    exit()
print(arr[k-1])