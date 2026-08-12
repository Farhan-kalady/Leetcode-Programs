class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        maxi = 0
        zeros = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            if zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            if zeros <= k:
                maxi = max(maxi, right - left + 1)
            right += 1
        return maxi        

        