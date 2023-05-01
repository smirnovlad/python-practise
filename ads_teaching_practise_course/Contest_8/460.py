def solve():
    n = int(input())
    gr = []
    for u in range(n):
        gr.append(list(map(int, input()[:-1].split(' '))))
        if gr[u][u]:
            print("NO")
            return
        for v in range(u):
            if gr[v][u] != gr[u][v]:
                print("NO")
                return
    print("YES")

solve()