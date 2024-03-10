n, m = map(int, input().split())
b = [input().split() for _ in range(n)]
result = 0
for r in range(n):
    cnt = 0
    t = b[r][0]
    for c in range(n):
        if b[r][c] == t:
            cnt += 1
        else:
            cnt = 1
            t = b[r][c]
        if cnt >= m:
            result += 1
            break
for c in range(n):
    cnt = 0
    t = b[0][c]
    for r in range(n):
        if b[r][c] == t:
            cnt += 1
        else:
            cnt = 1
            t = b[r][c]
        if cnt >= m:
            result += 1
            break
print(result)