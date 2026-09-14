class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        cur_sum = sum(nums)
        expec_sum = (n*(n + 1))//2
        missing = expec_sum - cur_sum
        return missing
        