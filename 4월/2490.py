for _ in range(3):
    bae, deng = 0, 0
    a, b, c, d = map(int, input().split())
    if a == 0:
        bae += 1
    else:
        deng += 1
    if b == 0:
        bae += 1
    else:
        deng += 1
    if c == 0:
        bae += 1
    else:
        deng += 1  
    if d == 0:
        bae += 1
    else:
        deng += 1  
    if bae == 0:
        print('E')
    elif bae == 1:
        print('A')
    elif bae == 2:
        print('B')
    elif bae == 3:
        print('C')
    elif bae == 4:
        print('D')