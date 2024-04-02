import sys
n = int(input())
a = list(map(int, input().split()))
MAX_INT = sys.maxsize
result = MAX_INT

for i in range(n):
    s = 0
    for j in range(n):
        if i == j:
            continue
        s += abs(i - j) * a[j]
    result = min(result, s)
print(result)