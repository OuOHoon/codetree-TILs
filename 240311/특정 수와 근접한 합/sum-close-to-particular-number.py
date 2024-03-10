import itertools

n, s = map(int, input().split())
numbers = list(map(int, input().split()))
sumv = sum(numbers)
result = 9999999
for comb in itertools.combinations(numbers, 2):
    result = min(result, abs(s - (sumv-sum(comb))))
print(result)