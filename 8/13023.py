a = [[0]*2000 for _ in range(2000)]
g = [[] for _ in range(2000)]
e = []
n, m = map(int, input().split())
for i in range(m):
    f, to = map(int, input().split())
    e.append((f, to))
    e.append((to, f))
    a[f][to] = True
    a[to][f] = True
    a[f][to], a[to][f] = 1, 1
    g[f].append(to)
    g[to].append(f)
    
for A, B in e:
    for C, D in e:
        if A == B or A==C or A==D or B==D or B==C or C==D:
            continue
        if not a[B][C]: continue
        for E in g[D]:
            if A==E or B==E or C==E or D==E:
                continue
            print(1)
            exit(0)
print(0)        