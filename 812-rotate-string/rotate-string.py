class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        n = len(s)
        sample = s
        for i in range(n):
            if sample == goal :
                return True
            sample = sample[-1] + sample[:-1]
        return False        
        