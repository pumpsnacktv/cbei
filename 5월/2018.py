n = int(input())
cnt = 1
start = 1
end = 1
sum = 1

while end != n:
    if sum < n:
        end += 1
        sum += end
    elif sum > n:
        sum -= start
        start += 1
    else:
        cnt += 1
        end += 1
        sum += end

print(cnt)