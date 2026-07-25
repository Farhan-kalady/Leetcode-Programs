class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        count = 0
        res = ""
        for i in s:
            if i == '(':
                count += 1
                if count > 1:
                    res += i
            else:
                count -= 1
                if count > 0:
                    res += i
        return res                 
