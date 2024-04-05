w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
p = (p+t)%(2*w)
q = (q+t)%(2*h)
if p > w:
    p = (w*2)-p
if q > h:
    q = (h*2)-q

print(p, q)
