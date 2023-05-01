n, m = map(int, input().split(' '))

ans = [None] * n

for i in range(m):
    u, v = map(int, input().split(' '))
    u -= 1
    v -= 1
    ans[u] = ans[u] + 1 if ans[u] else 1
    ans[v] = ans[v] + 1 if ans[v] else 1

for val in ans:
    print(val if val else 0, end=' ')