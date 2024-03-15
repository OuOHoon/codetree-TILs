n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]
maxK = 0
for row in grid:
    maxK = max(maxK, max(row))
visit = [[False] * m for _ in range(n)]
dys, dxs = [-1, 0, 1, 0], [0, 1, 0, -1]
def dfs(curr):
    global visit
    y, x = curr
    for dy, dx in zip(dys, dxs):
        ny, nx = y + dy, x + dx
        if 0 <= ny < n and 0 <= nx < m and grid[ny][nx] > k and not visit[ny][nx]:
            visit[ny][nx] = True
            dfs((ny, nx))
maxCnt = 0
result = 0
cnt = 0
for k in range(1, maxK+1):
    visit = [[False] * m for _ in range(n)]
    cnt = 0
    for r in range(n):
        for c in range(m):
            if grid[r][c] > k and not visit[r][c]:
                cnt += 1
                visit[r][c] = True
                dfs((r, c))
    if cnt > maxCnt:
        result = k
        maxCnt = cnt
print(result, maxCnt)