n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

def f(curr):
    y, x = curr
    if dp[y][x] == 0:
        if y == 0 and x == n-1:
            return mat[y][x]
        
        if y == 0:
            dp[y][x] = f((y, x+1)) + mat[y][x]
        elif x == n-1:
            dp[y][x] = f((y-1, x)) + mat[y][x]
        else:
            dp[y][x] = min(f((y-1, x)), f((y, x+1))) + mat[y][x]
    return dp[y][x]
f((n-1, 0))
print(dp[n-1][0])