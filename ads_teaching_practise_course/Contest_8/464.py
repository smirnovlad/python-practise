def solve():
    n = int(input())
    for u in range(n):
        l = list(map(int, input()[:-1].split(' ')))
        for v in range(n):
            if l[v] and v > u:
                print(u + 1, v + 1)

solve()