n = [0]*31
for i in range(28):
    temp = int(input())
    n[temp] = 1

for idx, i in enumerate(n):
    if i == 0:
        print(idx)


