# solution 1 暴力循环法
def rotate(nums, k):
    for i in range(k):
        temp_last = nums[len(nums) - 1]
        for j in range(len(nums)):
            temp = nums[j]
            nums[j] = temp_last
            temp_last = temp


# solution 2
def rotate2(nums, k):
    if len(nums) < 2:
        return
    temp = []
    for i in range(len(nums)):
        if i < k:
            temp.append(nums[len(nums) - k + i])
        else:
            temp.append(nums[i - k])

    for j in range(len(nums)):
        nums[j] = temp[j]


if __name__ == "__main__":
    list = [1, 2, 3, 4, 5, 6, 7]
    rotate2(list, 2)
    print(list)
