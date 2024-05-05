a, b, c, n = map(int, input().split())
flag = False
for i in range(0, 301):
    for j in range(0, 301):
        for k in range(0, 301):
            if i * a + j * b + k * c > n:
                flag = True
                break;
            if i * a + j * b + k * c == n:
                print(1)
                exit()
        flag = False

print(0)