class Solution:
    def maxDepth(self, s: str) -> int:
        max_brac = 0
        curr_brac = 0
        for brac in s:
            if brac == "(" :
                curr_brac += 1
                max_brac = max(max_brac, curr_brac)
            elif brac == ")":
                curr_brac -= 1
    
        return max_brac       