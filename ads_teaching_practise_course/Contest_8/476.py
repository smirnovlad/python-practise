def solve():
    n, m = map(int, input().split(' '))

    if m < n * (n - 1) / 2:
        print("NO")
        return

    gr = [[False for _ in range(n)] for _ in range(n)]

    for _ in range(m):
        u, v = map(int, input().split(' '))
        u -= 1
        v -= 1
        gr[u][v] = True
        gr[v][u] = True

    for u in range(n):
        if sum(gr[u]) != n - 1:
            print("NO")
            return

    print("YES")

solve()