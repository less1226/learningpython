def singleNumber(self, nums: List[int]) -> int:
        return_value = nums[0]
        if len(nums)==1:
            return nums[0]
        
        nums.sort()
        for i in range(len(nums)):
            if i == 0:
                if nums[i] != nums[i+1]:
                    return_value = nums[i]
            elif i+1 == len(nums):
                if nums[i] != nums[i-1]:
                    return_value = nums[i]
            else:
                if nums[i] != nums[i-1] and nums[i]!=nums[i+1]:
                    return_value = nums[i]
        
        return return_value
