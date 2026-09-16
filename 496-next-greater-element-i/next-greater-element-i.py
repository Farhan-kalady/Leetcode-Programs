class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack = []
        result = {}

        for num in nums2:
            while stack and num > stack[-1]:
                smaller = stack.pop()
                result[smaller] = num
            stack.append(num)
        while stack:
            result[stack.pop()] = -1
        return [result[num] for num in nums1]