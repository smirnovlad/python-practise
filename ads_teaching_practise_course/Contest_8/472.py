def solve():
    n = int(input())

    result = [[0, 0] for _ in range(n)]

    # gr = [[0 for _ in range(n)] for _ in range(n)]

    for u in range(n):
        l = list(map(int, input()[:-1].split(' ')))
        for v in range(n):
            if l[v]:
                result[u][1] += 1
                result[v][0] += 1
    for l in result:
        for val in l:
            print(val)

solve()