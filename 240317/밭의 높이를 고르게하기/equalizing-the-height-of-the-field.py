n, h, t = map(int, input().split())
heights = list(map(int, input().split()))
result = 999999
for i in range(n):
    cost = 0
    for j in range(i, min(n, i + t)):
        cost += abs(heights[j] - h)
    result = min(cost, result)
print(result)