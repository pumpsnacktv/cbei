s = input()
cm = 0
for i in range(0, len(s)):
    if i == 0:
        cm += 10
    elif s[i-1] == s[i]:
        cm += 5
    else:
        cm += 10
print(cm)