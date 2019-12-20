class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        presub = nums[0]
        maxsub = nums[0]
        for i in nums[1:]:
            presub = max(i, presub + i)
            maxsub = max(maxsub, presub)

        return maxsub