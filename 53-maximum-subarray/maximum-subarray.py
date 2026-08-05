class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        cur_sum  = 0
        best = float('-inf')
        for num in nums[:]:
            cur_sum += num
            best = max(best, cur_sum)
            if cur_sum < 0:
                cur_sum = 0

        return best        
                   
              

