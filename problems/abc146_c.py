# 二分探索

import math


def binary_search(min_n: int, max_n: int, a: int, b: int, x: int) -> int:
    def val_fun(a: int, b: int, n: int) -> int:
        return a * n + b * len(str(n))

    # 最小値と最大値が1未満になるように調整
    while max_n-min_n > 1:

        # 最小値と最大値の半分 最小の整数を求めるので切り捨て
        n = (min_n + max_n)//2

        # A×N + B×len(N) が x以下で最低となるようなNを見つける
        val = val_fun(a, b, n)

        # 購入できる場合はnを最小値に更新する
        if val <= x:
            min_n = n

        # 購入できない場合はnを最大値とする
        else:
            max_n = n

    return min_n


def main():
    list_a = list(map(int, input().split()))
    a, b, x = list_a[0], list_a[1], list_a[2]
    n = binary_search(0, 10**9+1, a, b, x)
    print(n)


if __name__ == '__main__':
    main()
