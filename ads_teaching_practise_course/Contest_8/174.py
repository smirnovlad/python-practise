n = int(input())

count = 0

for i in range(n):
    l = list(map(int, input()[:-1].split(' ')))
    for j in range(i):
        count += l[j]

print(count)