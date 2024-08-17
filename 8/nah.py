def checker(password):
    mo, ja = 0, 0
    for c in password:
        if c in "aeiou":
            mo += 1
        else:
            ja += 1
    return mo >= 1 and ja >= 2


def recu(n, alpha, password, i):
    if len(password)==n:
        if checker(password):
            print(password)
        return
    if len(alpha)<=i:
        return
    
    recu(n, alpha, password+alpha[i], i+1)
    recu(n, alpha, password, i+1)


l, c = map(int, input().split())
s = input().split()
s = sorted(s)

recu(l, s, "", 0)