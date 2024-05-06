m, n = map(int, input().split())
ans = 0
uni = []
for i in range(m):
    uni.append(list(map(int,input().split())))

for i in range(m-1): 
    for j in range(i+1, m):
        flag = True
        for k in range(n-1): #
            for l in range(k+1, n):
                if uni[i][k] > uni[i][l] and not uni[j][k] > uni[j][l]:
                    flag = False
                    break
                if uni[i][k] == uni[i][l] and not uni[j][k] == uni[j][l]:
                    flag = False
                    break
                if uni[i][k] < uni[i][l] and not uni[j][k] < uni[j][l]:
                    flag = False
                    break
            if not flag:
                break
        if flag:
            ans += 1

print(ans)

                