import numpy as np
import itertools as itr


n = int(input())

def ditect(n:int) -> int:
    counter = 0
    if n > 1000 or not isinstance(n, int):
        print("Miss")
    else:
        nums = []

        for i in range(n):
            x, y = input().split()
            x, y = int(x), int(y)
            if not abs(x) > 1000 or abs(y) > 1000 or not isinstance(x or y, int):
                nums.append(np.array([x,y]))

        all_list = itr.combinations(nums, 2)

        for x in all_list:
            if abs((x[1][1] - x[0][1])/(x[1][0] - x[0][0]))<=1:
                counter += 1
    return counter

def main():
    count = ditect(n)
    print(count)


if __name__ == '__main__':
    main()
