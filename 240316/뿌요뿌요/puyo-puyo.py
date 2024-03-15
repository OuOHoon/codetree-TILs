n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
cnt, maxSize = 0, 0
c = 0
visit = [[False] * n for _ in range(n)]
dys, dxs = [-1, 0, 1, 0], [0, 1, 0, -1]
def dfs(curr):
    global visit, c
    y, x = curr

    for dy, dx in zip(dys, dxs):
        ny, nx = y + dy, x + dx
        if 0 <= ny < n and 0 <= nx < n and not visit[ny][nx] and grid[y][x] == grid[ny][nx]:
            visit[ny][nx] = True
            c += 1
            dfs((ny, nx))

for i in range(n):
    for j in range(n):
        if not visit[i][j]:
            c = 1
            visit[i][j] = True
            dfs((i, j))
            if c >= 4:
                cnt += 1
            maxSize = max(maxSize, c)

print(cnt, maxSize)