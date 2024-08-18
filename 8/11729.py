n = int(input())
t = []
def r(a, b, c, n):
    if n == 1:
        t.append([a, c])
        return
    
    r(a, c, b, n-1) 
    t.append([a, c])
    r(b, a, c, n-1)

r(1, 2, 3, n)
print(len(t))
for i in t:
    print(i[0], i[1])