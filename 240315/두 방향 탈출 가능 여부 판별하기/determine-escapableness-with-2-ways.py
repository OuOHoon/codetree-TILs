n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

d = [(1, 0), (0, 1)]
visit = [[False] * n for _ in range(n)]
can = 0
def dfs(curr):
    y, x = curr
    if y == n-1 and x == n-1:
        can = 1
        return None
        
    for dyx in d:
        dy, dx = dyx
        ny, nx = y + dy, x + dx
        if 0 <= ny < n and 0 <= nx < n and grid[ny][nx] != 0 and not visit[ny][nx]:
            visit[ny][nx] = True
            dfs((ny, nx))
visit[0][0] = True
dfs((0, 0))
print(can)