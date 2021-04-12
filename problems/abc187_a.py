a, b = input().split()
a = [int(a[i]) for i in range(len(a))]
b = [int(b[i]) for i in range(len(b))]

if sum(a) >= sum(b):
    print(sum(a))
else:
    print(sum(b))

