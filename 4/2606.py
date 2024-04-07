import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
arr = [[] for _ in range(n+1)]
visit = [0 for _ in range(n+1)]

def dfs(a):
    if visit[a]:
        return
    visit[a] = 1
    for i in arr[a]:
        dfs(i)

for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    arr[s].append(e)
    arr[e].append(s)

dfs(1)
print(sum(visit)-1)