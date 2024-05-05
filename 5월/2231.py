n = int(input())

for i in range(1, n):
    temp = i
    ans = i
    while temp != 0:
        ans += (temp % 10)
        temp //= 10
    if ans == n:
        print(i)
        exit()

print(0)