def solve():
    n = int(input())

    count = 0

    for u in range(n):
        l = list(map(int, input()[:-1].split(' ')))
        for v in range(u + 1):
            count += l[v]

    print(count)

solve()