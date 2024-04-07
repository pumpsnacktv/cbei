n = int(input())

p = list(map(int, input().split()))

p.sort()
ans = 0
ans2 = 0
for i in p:
    ans += i
    ans2 += ans

print(ans2)