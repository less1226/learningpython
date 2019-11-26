from typing import List


def moveZeroes(nums: List[int]) -> None:
    """
        Do not return anything, modify nums in-place instead.
        """
    step = 0
    current = 0
    non_zero = 0
    length = len(nums)
    if length == 1:
        return

    for i in range(length):
        if current == length:
            break

        if nums[current] == 0:
            step += 1
            current += 1
            continue

        nums[non_zero] = nums[non_zero + step]
        non_zero += 1
        current += 1

    if step > 0:
        for j in range(step):
            nums[length - 1 - j] = 0
