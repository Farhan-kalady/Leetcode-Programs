class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        my_set = set()
        for i in range(len(nums)):
            if nums[i] in my_set:
                return True
            my_set.add(nums[i])
        return False        