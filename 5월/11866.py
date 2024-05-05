from collections import deque
n, k = map(int, input().split())

de = deque([])
for i in range(1, n+1):
    de.append(i)
print('<',end='')

while len(de) != 1:
    for _ in range(k-1):
        de.append(de.popleft())
    print(de.popleft(), end=", ")

print(de.pop(), end='')
print('>')