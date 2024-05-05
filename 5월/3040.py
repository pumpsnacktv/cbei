arr = []
for _ in range(9):
    arr.append(int(input()))
s = sum(arr) - 100
q,w = 0, 0

for i in range(0, 9):
    for j in range(0, 9):
        if arr[i]+arr[j] == s:
            q, w = i, j

for i in range(9):
    if i != q and i != w:
        print(arr[i])