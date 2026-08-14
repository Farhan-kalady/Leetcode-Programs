class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        n = len(nums)
        left = 0
        nums.sort()
        right = n - 1
        while left < right:
            total = nums[left] + nums[right]
            if total == k:
                count += 1
                left += 1
                right -= 1
            elif total < k:
                left += 1
            else:
                right -= 1
        return count                 
                  