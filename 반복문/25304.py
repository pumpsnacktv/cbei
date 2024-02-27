a = int(input())
b = int(input())
result = 0
for item in range(1, b+1):
    temp1, temp2 = map(int, input().split())
    result += temp1 * temp2

if result != a:
    print('No')
else:
    print('Yes')
