arr = []
for _ in range(5):
    arr.append(int(input()))
av = sum(arr)//5
arr.sort()
print(av)
print(arr[2])