# 純烈全探索を使う問題

import itertools as itr


def zentan(l: list) -> list:
    nnn = list(itr.permutations(l))
    return nnn


def calc(nnn: list) -> None:
    calc_ = []
    for i in range(2):

        num_tup = tuple(map(int, input().split()))
        tmp_num = 0

        for j in range(len(nnn)):

            if nnn[j] == num_tup:
                tmp_num = j+1
                calc_.append(tmp_num)
    print(abs(calc_[0]-calc_[1]))


def main():
    n = int(input())
    if n <2 or n>8 or not isinstance(n,int):
        print("error")
        return
    n_ = [i+1 for i in range(n)]
    nnn = zentan(n_)
    calc(nnn)


if __name__ == '__main__':
    main()
