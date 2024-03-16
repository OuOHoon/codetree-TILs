n, h, t = map(int, input().split())
heights = list(map(int, input().split()))
result = 999999
for i in range(n - t + 1):
    cost = 0
    if i + t > n:
        continue
    for j in range(i, i + t):
        cost += abs(heights[j] - h)
    result = min(cost, result)
print(result)