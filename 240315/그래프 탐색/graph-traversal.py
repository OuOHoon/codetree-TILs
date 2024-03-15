n, m = map(int, input().split())

g = {i:set([]) for i in range(n+1)}
for _ in range(m):
    x, y = map(int, input().split())
    g[x].add(y)
    g[y].add(x)
visit = [False for _ in range(n+1)]

def dfs(cur):
    for nextNode in g[cur]:
        if not visit[nextNode]:
            visit[nextNode] = True
            dfs(nextNode)
            
visit[1] = True
dfs(1)
print(sum(visit)-1)