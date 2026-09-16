class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = 0
        maxi = float('-inf')
        for num in nums:
            cur += num
            maxi = max(maxi, cur)
            if cur < 0:
                cur = 0
        return maxi             


              

