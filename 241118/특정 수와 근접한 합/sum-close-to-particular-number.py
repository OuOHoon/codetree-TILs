import itertools

_, s = map(int, input().split())
n = list(map(int, input().split()))
total = sum(n)
result = 100000
for comb in itertools.combinations(n, 2):
    if abs(s - (total - sum(comb))) < result:
        result = abs(s - (total - sum(comb)))
print(result)
