n = [0]*42
for i in range(10):
    a = int(input())
    n[a % 42] = 1
c = 0
for i in range(42):
    if n[i] == 1:
        c += 1

print(c)