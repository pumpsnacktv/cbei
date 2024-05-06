t = int(input())

for _ in range(t):
    s = input()
    l = []
    r = []
    for i in s:
        if i == '<':
            if l:
                r.append(l.pop())
        elif i == '>':
            if r:
                l.append(r.pop())
        elif i == '-':
            if l:
                l.pop()
        else:
            l.append(i)
    l.extend(reversed(r))
    for i in l:
        print(i, end='')
    print()

