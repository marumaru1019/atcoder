# bit全探索で得問題

def bit_full_search_calc(item: list) -> list:
    bags = []
    # 2^n(種類数)
    for i in range(2**len(item)):
        bag = []
        for j in range(len(item)):
            if ((i >> j) & 1):  # 最下位のけたが①であるかチェック
                bag.append("+")  # フラグが立っていたら bag に果物を詰める
            else:
                bag.append("-")
        bags.append(bag)
    return bags


def calc(calc_item: list, num: str) -> list:
    apply_list = []

    for i in range(len(calc_item)):

        tmp_num = int(num[0])
        tmp_list = [num[0]]

        for j in range(len(calc_item[i])):
            if calc_item[i][j] == "+":
                tmp_num += int(num[j+1])
                tmp_list.append("+")
                tmp_list.append(num[j+1])
            elif calc_item[i][j] == "-":
                tmp_num -= int(num[j+1])
                tmp_list.append("-")
                tmp_list.append(num[j+1])

        if tmp_num == 7:
            apply_list.append(tmp_list)
        else:
            pass

    return apply_list


def main():
    num = input()
    item = ["", "", ""]
    patt = bit_full_search_calc(item)
    apply_list = calc(patt, num)
    print(f'{"".join(apply_list[0])}=7')


if __name__ == '__main__':
    main()
