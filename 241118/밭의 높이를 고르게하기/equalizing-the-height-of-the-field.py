import sys
INT_MAX = sys.maxsize
n, h, t = map(int, input().split())
farms = list(map(int, input().split()))

new_farms = [abs(f - h) for f in farms]
result = INT_MAX
for i in range(n - t + 1):
    cost = 0
    for j in range(i, i+t):
        cost += new_farms[j]
    result = min(result, cost)
print(result)