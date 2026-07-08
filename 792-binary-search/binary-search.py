class Solution(object):
    def search(self, nums, target):
        
        
        def bst(low, high):
            if low > high:
                return -1
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return bst(mid + 1, high)
            else:
                return bst(low, mid - 1)   
        return bst(0, len(nums) - 1)               

        