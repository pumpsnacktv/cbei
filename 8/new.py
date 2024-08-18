def r(cnt,n):
    if cnt == n:
        return
    r(cnt+1, n)
    print(cnt)
r(0, int(input()))