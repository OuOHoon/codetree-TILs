n, m = map(int, input().split())
b = [input().split() for _ in range(n)]
result = 0
for r in range(n):
    cnt = 1
    t = b[r][0]
    for c in range(1, n):
        if b[r][c] == t:
            cnt += 1
            if cnt >= m:
                result += 1
                break
        else:
            cnt = 1
            t = b[r][c]
for c in range(n):
    cnt = 1
    t = b[0][c]
    for r in range(1, n):
        if b[r][c] == t:
            cnt += 1
            if cnt >= m:
                result += 1
                break
        else:
            cnt = 1
            t = b[r][c]
print(result)