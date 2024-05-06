s = input()
st = []
cnt = 0
for i in range(len(s)):
    if s[i] == '(':
        st.append('(')
    elif s[i] == ')':
        if s[i-1] == '(':
            st.pop()
            cnt += len(st)
        else:
            st.pop()
            cnt += 1

print(cnt)