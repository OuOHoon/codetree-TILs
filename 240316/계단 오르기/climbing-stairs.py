n = int(input())
dp = [-1] * (n + 1)
def f(floor):
    if floor == 0:
        return 1
    if floor < 2:
        return 0
    
    if dp[floor] == -1:
        dp[floor] = (f(floor - 2) + f(floor - 3)) % 10007
    return dp[floor]

f(n)
print(dp[n])