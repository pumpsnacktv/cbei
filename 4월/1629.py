a,b,c = map(int, input().split())

def power(a , b , c):
    if b == 1:
        return a % c
    if b % 2:
        return a * power(a, b-1, c) % c
    else:
        return (power(a, b/2, c) ** 2) % c

print(power(a,b,c))