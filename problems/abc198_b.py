n = input()
n_ = [n[i] for i in range(len(n))]

if n_ == n_[::-1]:
    print("Yes")

else:
    n_[0:0] = ["0"]
    if n_ == n_[::-1]:
        print("Yes")
    else:
        print("No")
