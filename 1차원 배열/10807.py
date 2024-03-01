n = int(input())
ans = 0
arr = map(int, input().split())
v = int(input())

for item in arr:
    if item == v:
        ans += 1
    
print(ans)