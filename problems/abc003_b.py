

def eaqul_str(s_:list, t_:list, wild_card_:list) -> str:

    for i in range(len(s_)):

        if s_[i] == t_[i]:
            pass

        elif s_[i] == "@":
            if t_[i] in wild_card_:
                pass
            else:
                return "You will lose"

        elif t_[i] == "@":
            if s_[i] in wild_card_:
                pass
            else:
                return "You will lose"

        else:
            return "You will lose"

    return "You can win"

def main():
    s = input()
    t = input()
    wild_card = "atcoder"

    # change to lise type
    s_ = [s[i] for i in range(len(s))]
    t_ = [t[i] for i in range(len(t))]

    wild_card_ = [wild_card[i] for i in range(len(wild_card))]
    judge_str = eaqul_str(s_,t_,wild_card)
    print(judge_str)


if __name__ == '__main__':
    main()
