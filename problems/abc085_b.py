# 重複チェックを行う関数

def judge_duplicaiton(loop_num:int) -> list:
    not_duplication = []
    for i in range(loop_num):
        num = int(input())
        if num not in not_duplication:
            not_duplication.append(num)
        else:
            pass
    return not_duplication

def main():
    n = int(input())
    not_duplication = judge_duplicaiton(n)
    print(len(not_duplication))


if __name__ == '__main__':
    main()
