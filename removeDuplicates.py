def removeDuplicates(self, nums):
    if nums == []: return 0
    left = 0
    for i in range (1, len(nums)):
        if nums[i] != nums[left]:
            left += 1
            nums[left] = nums[i]
    del nums[left+1:]
    return left + 1
