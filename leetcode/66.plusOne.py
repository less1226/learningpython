from typing import List


def plusOne(digits: List[int]) -> List[int]:
    for i in range(len(digits) - 1, -1, -1):
        digits[i] += 1
        if digits[i] > 9:
            digits[i] = 0
            if i == 0:
                digits = [1] + digits
        else:
            break

    return digits


if __name__ == "__main__":
    test_list = [4, 3, 2, 1]
    result = plusOne(test_list)
    print(result)