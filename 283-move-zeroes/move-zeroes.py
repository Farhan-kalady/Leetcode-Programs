class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 1:
            return
        i = 0
        while i < n:
            if nums[i] == 0:
                break
            i += 1
        if i == n:
            return
        j = i + 1

        while j < n:
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]   
                i += 1
            j += 1                