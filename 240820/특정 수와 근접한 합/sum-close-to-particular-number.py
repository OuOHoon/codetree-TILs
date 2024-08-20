n, s = map(int, input().split())
arr = list(map(int, input().split()))
result = 100000
maximun = sum(arr)

for i in range(len(arr)-1):
    for j in range(i ,len(arr)):
        ex = maximun - (arr[i] + arr[j])
        result = min(result, abs(s - ex))
print(result)