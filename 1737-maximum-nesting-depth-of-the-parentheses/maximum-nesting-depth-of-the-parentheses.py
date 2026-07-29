class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_depth = 0
        curr_depth =0
        for brac in s:
            if brac == '(':
                curr_depth += 1
                max_depth = max(max_depth, curr_depth)
            elif brac == ')':
                curr_depth -= 1
        return max_depth            