arr = []
for _ in range(9):
    arr.append(int(input()))
_sum = sum(arr)
arr.sort()

for i in range(9):
    for j in range(i+1, 9):
        check = _sum - arr[i] - arr[j]
        if check == 100:
            for k in range(9):
                if k != i and k != j:
                    print(arr[k])
            exit()