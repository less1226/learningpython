from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    dic = {}
    for i in range(len(nums)):
        if target - nums[i] in dic:
            return [dic[target - nums[i]], i]
        dic[nums[i]] = i
    return []


if __name__ == "__main__":
    result = twoSum([-3,1,3], 0)
    print(result)