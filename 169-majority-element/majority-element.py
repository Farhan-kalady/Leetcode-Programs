class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        my_dict = {}
        for num in nums:
            my_dict[num] = my_dict.get(num, 0)+1
        return max(my_dict, key=my_dict.get)