class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def dfs(index, subset):
            if index == len(nums):
                res.append(list(subset))
                return 
            subset.append(nums[index])
            dfs(index + 1, subset)
            subset.pop()
            dfs(index + 1, subset)    
        dfs(0,[])
        return res           


        
        