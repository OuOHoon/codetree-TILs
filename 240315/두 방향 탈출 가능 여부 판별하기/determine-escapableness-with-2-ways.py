n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

d = [(1, 0), (0, 1)]
visit = [[False] * m for _ in range(n)]

def dfs(curr):
    y, x = curr
    for dyx in d:
        dy, dx = dyx
        ny, nx = y + dy, x + dx
        if 0 <= ny < n and 0 <= nx < m and grid[ny][nx] == 1 and not visit[ny][nx]:
            visit[ny][nx] = True
            dfs((ny, nx))
visit[0][0] = True
dfs((0, 0))
print(1 if visit[n-1][m-1] else 0)