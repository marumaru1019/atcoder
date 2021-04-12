n,y = map(int,input().split())


def get_patt(n:int,y:int) -> list:

    # 区切りの数でプラス位置しないと2000枚にしても 1999枚で止まってしまうので注意
    for i in range(n+1):
        for j in range(n-i+1):
            kei = sum([10000*i, 5000*j, 1000*(n-i-j)])
            if kei == y:
                return [str(i),str(j),str(n-i-j)]
            else:
                pass
    return [str(-1),str(-1),str(-1)]


print(" ".join(get_patt(n, y)))

