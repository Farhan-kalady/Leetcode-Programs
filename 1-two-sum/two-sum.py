class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for index, value in enumerate(nums):
            need = target - value
            if need in hash_map:
                return [index, hash_map[need]]
            else:
                hash_map[value] = index
        return -1        
