class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        nums = sorted(nums)
        left = 0
        right = 1
        while right < n:
            if nums[left] == nums[right]:
                return True
            else:
                left += 1
                right += 1
        return False            
            