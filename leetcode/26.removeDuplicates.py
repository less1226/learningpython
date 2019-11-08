def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = 0
    for i in range(1, len(nums)):
        if nums[n] != nums[i]:
            nums[n + 1] = nums[i]
            n = n + 1

    return n + 1


if __name__ == "__main__":
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 4]
    n = removeDuplicates(nums)
    print(nums[:n])