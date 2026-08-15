class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_num = sum(nums)
        miss = (n*(n + 1)) // 2 - sum_num
        return miss