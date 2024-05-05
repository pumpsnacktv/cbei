n, m = map(int, input().split())

g = 0
for i in range(1, m+1):
    if n % i == 0 and m % i == 0:
        if g < i:
            g = i

print(g)
print(n*m//g)