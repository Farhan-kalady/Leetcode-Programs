class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        total = 0
        while l < r:
            width = r - l
            hight = min(height[l], height[r])
            area = hight * width
            total = max(total, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return total            