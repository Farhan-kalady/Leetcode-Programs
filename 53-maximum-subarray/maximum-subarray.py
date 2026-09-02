class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur = 0
        maxi = float('-inf')
        for i in range(len(nums)):
            cur += nums[i]
            maxi = max(maxi, cur)
            if cur < 0:
                cur = 0
        return maxi        