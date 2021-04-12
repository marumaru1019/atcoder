n = int(input())

def judge(n:int) -> str:
    if n >=1 and n<2*10**5 and isinstance(n, int):
        fonts = []
        for i in range(n):
            fonts.append(input())

        fonts_mirror = ["!"+fonts[i] for i in range(len(fonts))]

        for j in fonts_mirror:
            if j in fonts:
                return j[1:]
            else:
                pass
        return "satisfiable"

    else:
        return "error"

def main():
    print(judge(n))


if __name__ == '__main__':
    main()

