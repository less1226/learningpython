def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = 1
    for i in range(1, len(nums)):
        for j in range(n):
            hasd = 1
            if nums[i] == nums[j]:
                hasd = 1
                break
            else:
                hasd = 0
        if hasd == 0:
            temp = nums[i]
            nums[i] = nums[n]
            nums[n] = temp
            n = n + 1

    return n


if __name__ == "__main__":
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 1, 2, 6, 4, 9, 8, 7]
    n = removeDuplicates(nums)
    print(nums[:n])