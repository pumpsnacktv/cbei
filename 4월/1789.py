s = int(input())

n = 1 
cnt = 0
ans = 0
while ans < s:
    ans += n
    n += 1
    cnt += 1
if ans > s:
    cnt -= 1

print(cnt)