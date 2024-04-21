import sys

n = int(input())
arr = []
for i in range(n):
    temp = int(input())
    arr.append(temp)

res = 0
st = [(-1, -1)]
for i in range(n+1):
    h, idx = arr[i], i
    while st[-1][0] >= h:
        res = max(res, st[-1][0] * (i - st[-1][1]))
        idx = st[-1][1]
        st.pop()
    st.append((h, idx))
print(res)
