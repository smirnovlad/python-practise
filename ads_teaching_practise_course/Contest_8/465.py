def solve():
    n, m = map(int, input().split(' '))

    gr = [[0 for _ in range(n)] for _ in range(n)]

    for _ in range(m):
        u, v = map(int, input().split(' '))
        u -= 1
        v -= 1
        gr[u][v] = gr[v][u] = 1

    for u in range(n):
        for v in range(n):
            print(gr[u][v], end=' ')
        print()

solve()