import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
dq = deque([])

for i in range(1, n+1):
    dq.append(i)

print('<', end='')
while len(dq):
    m = k % len(dq)
    for _ in range(m):
        dq.append(dq[0])
        dq.popleft()
    print(dq[-1], end='')
    if len(dq) != 1:
        print(end=', ')
    else:
        print('>')
    dq.pop()
