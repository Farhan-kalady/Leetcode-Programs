class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        hashmap = {}
        for index, value in enumerate(nums):
            compliment = nums[index]
            if compliment in hashmap:
                return True
            else:
                hashmap[value] = index
        return False            
                     