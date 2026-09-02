class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i, value in enumerate(nums):
            need = target - nums[i]
            if need in hashmap:
                return [i, hashmap[need]]
            else:    
                hashmap[value] = i    
