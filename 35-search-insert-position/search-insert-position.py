class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        left = 0
        right = n - 1
        lb = n
        while left <= right :
            mid = (left + right) // 2
            if nums[mid] >= target:
                lb = mid
                right = mid - 1
            else:
                left = mid + 1
        return lb            
        