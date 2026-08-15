class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        nums.sort()
        n = len(nums)
        left = 0
        right = n - 1
        while left < right:
            if nums[left] + nums[right] == k:
                count += 1
                left += 1
                right -= 1
            elif nums[left] + nums[right] < k :
                left += 1
            else:
                right -= 1
        return count                


                       
                  