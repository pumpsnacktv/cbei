n = int(input())

for i in range(n):
    s = input()
    arr = []
    cnt = 0
    for j in range(0, len(s)):
        if s[j] == '(':
            arr.append('(')
            cnt += 1
        elif s[j] == ')':
            if len(arr) == 0:
                arr.append(')')
            elif cnt == 0:
                arr.append(')')
            else:
                arr.pop()
                cnt -= 1
    if len(arr) == 0:
        print("YES")
    else:
        print("NO")