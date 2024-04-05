import sys
n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
m = int(input())
arr2 = list(map(int, sys.stdin.readline().split()))
arr.sort()
for i in arr2:
    left = 0
    right = n-1
    flag = False
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == i:
            print(1)
            flag = True
            break
        elif arr[mid] > i:
            right = mid-1
        elif arr[mid] < i:
            left = mid+1
    if not flag:
        print(0)