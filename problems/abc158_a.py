t = input()
t_l = [t[i] for i in range(len(t))]


first = t_l[0]
judge = "No"

for i in range(len(t_l)-1):
    if first != t_l[i+1]:
        judge = "Yes"

print(judge)
