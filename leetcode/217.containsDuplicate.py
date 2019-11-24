def containsDuplicate(nums: List[int]) -> bool:
    tempDict = {}
    for i in range(len(nums)):
        if nums[i] in tempDict:
            return True
        else:
            tempDict[nums[i]] = nums[i]

    return False
