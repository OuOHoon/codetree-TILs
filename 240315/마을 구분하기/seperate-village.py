n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

result = []
dys, dxs = [-1, 0, 1, 0], [0, 1, 0, -1]
visit = [[False] * n for _ in range(n)]
cnt = 0
def dfs(curr):
    global cnt
    y, x = curr
    for dy, dx in zip(dys, dxs):
        ny, nx = y + dy, x + dx
        if 0 <= ny < n and 0 <= nx < n and grid[ny][nx] == 1 and not visit[ny][nx]:
            visit[ny][nx] = True
            cnt += 1
            dfs((ny, nx))
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and not visit[i][j]:
            visit[i][j] = True
            cnt = 1
            dfs((i, j))
            result.append(cnt)
print(len(result))
for i in sorted(result):
    print(i)