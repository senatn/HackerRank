n = int(input())
d = {}
for i in range(n):
    world = input()
    if world not in d:
        d[world]= 1
    else:
        d[world] += 1

print(len(d))
for i in d:
    print(d[i], end=' ')