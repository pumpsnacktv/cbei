n = []
for i in range(10):
    a = int(input())
    if not a%42 in n:
        n.append(a%42)

print(len(n))


