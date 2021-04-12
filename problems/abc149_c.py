import math


def judge_prime(target: int) -> bool:
    max_div = math.ceil(math.sqrt(target))

    div_list = [i+1 for i in range(max_div)]

    # 1が入ってしまうため[1:]とする
    for div in div_list[1:]:
        if target % div == 0:
            return False

    return True


def prime_loop(n: int) -> int:

    if n > 10**5 or n < 2:
        return 0

    first_num = n

    if first_num == 2:
        return 2

    while True:
        if judge_prime(first_num):
            return first_num
        else:
            first_num += 1


def main():
    n = int(input())
    nn = prime_loop(n)
    print(nn)


if __name__ == '__main__':
    main()
