class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        total = 0
        while left < right:
            width = right - left
            cur_height = min(height[left], height[right])
            area = width * cur_height

            total = max(total, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return total            