n = int(input())
k = int(input())

total = 1
for i in range(n):
    if total < k:
        total *= 2
    else:
        total += k

print(total)
