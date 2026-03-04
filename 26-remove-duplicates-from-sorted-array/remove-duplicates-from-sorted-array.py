class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if nums == 0:
            return 0

        k = 1
        prev = nums[0]

        for i in range(1, n):
            x = nums[i]
            if x != prev:
                nums[k] = x
                prev = x
                k += 1
        return k             

