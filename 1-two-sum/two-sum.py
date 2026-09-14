class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for index, value in enumerate(nums):
            compliment = target - value
            if compliment in hashmap:
                return [index,hashmap[compliment]]
            else:
                hashmap[value] = index
        return -1        
           
