class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        expect = n * (n + 1) // 2
        actual = sum(nums)
        return expect - actual