# k개의 선이 있음. 이 선으로 모든 사람의 좌표를 덮어야함. 사람과 사람 사이가 거리가 가장 먼 곳을 이어야 하는 경우가 있을까? 없다. 가장 먼 곳 k-1개만큼 자르자

n, k = map(int, input().split())

if (k >= n):
    print(0)
else:
    location = list(set(sorted(list(map(int, input().split())))))

    result = location[-1] - location[0]
    temp_location = location[0]
    distances = []
    for idx, l in enumerate(location[1:]):
        distances.append((idx, l - temp_location))
        temp_location = l
    distances.sort(key=lambda x: x[1], reverse=True)

    for i in range(k-1):
        result -= distances[i][1]

    print(result)