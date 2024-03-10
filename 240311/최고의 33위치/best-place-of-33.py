n = int(input())
b = [input().split() for _ in range(n)]
p = []
for i in range(n):
    for j in range(n):
        if b[i][j] == '1':
            p.append((i, j))
result = 0
for yx in p:
    y, x = yx
    cnt = 0
    for r in range(y, min(y+3, n)):
        for c in range(x, min(x+3, n)):
            if b[r][c] == '1':
                cnt += 1
    result = max(cnt, result)
print(result)