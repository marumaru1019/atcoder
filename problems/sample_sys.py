from sys import stdin


# 一行入力の場合
def first():
    readline = stdin.readline
    A, B = map(int, readline().split())
    print(f"{A},{B}")


def make_list():
    readline = stdin.readline
    unko = list(map(str, readline().split()))
    print(unko)

# first()
make_list()
