class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i, value in enumerate(nums):
            compliment = target - value
            if compliment in hashmap:
                return [i, hashmap[compliment]]
            else:
                hashmap[value] = i
        return -1            
              
           
