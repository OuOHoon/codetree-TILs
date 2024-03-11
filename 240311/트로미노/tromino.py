n, m = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(n)]

ttr = [((-1, 0), (0, 1)), ((-1, 0), (0, -1)), ((0, -1), (1, 0)), ((1, 0), (0, 1))]
llr = [((0, 1), (0, 2)), ((1, 0), (2, 0))]

def is_inner(r, c):
    return 0 <= r < n and 0 <= c < m

result = 0
for r in range(n):
    for c in range(m):
        for tt in ttr:
            is_in = True
            s = b[r][c]
            for t in tt:
                ty, tx = t
                if not is_inner(r + ty, c + tx):
                    is_in = False
                    break
                s += b[r+ty][c+tx]
            if is_in:
                result = max(result, s)
        for ll in llr:
            is_in = True
            s = b[r][c]
            for l in ll:
                ty, tx = l
                if not is_inner(r + ty, c + tx):
                    is_in = False
                    break
                s += b[r+ty][c+tx]
            if is_in:
                result = max(result, s)

print(result)