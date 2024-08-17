n = int(input())

l = [list(map(int, input().split())) for _ in range(n)]
def cal_val(t):
    val = 0
    for i in t:
        for j in t:
            val += l[i][j]
    return val

def recursion(idx, start, link):
    if idx==n:
        if len(start) != n//2:
            return 999999
        if len(link) != n//2: 
            return 999999
        startv = cal_val(start)
        linkv = cal_val(link)
        diff = startv-linkv
        if diff<0:
            diff = diff*-1
        return diff 
    ans = 999999
    ans = min(ans, recursion(idx+1, start+[idx], link))
    ans = min(ans, recursion(idx+1, start, link+[idx]))
    return ans
print(recursion(0, [], []))