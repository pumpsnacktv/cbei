def recu(day, sum):
    if day == n:
        return sum
    if day>n: return 0

    ans = max(ans, recu(day+t[day], sum+v[day]))
    ans = max(ans, recu(day+1, sum))
    return ans
ans = 0
n = int(input())
t, v = [], []

for _ in range(n):
    tt, vv = map(int, input().split())
    t.append(tt)
    v.append(vv)

print(recu(0, 0))
    
# n = int(input())
# m = -1
# arr = []
# for _ in range(n):
#     arr.append(list(map(int, input().split())))

# def recu(day,cash):
#     if day == n+1:
#         m = max(m, cash)
#         return
#     if arr[day][0] + day <= n-1:
#         recu(day+arr[day][0], cash+arr[day][1])
#     else:
#         recu(day+1, cash)

# recu(0, arr, 0)

# print(m)