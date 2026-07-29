class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        letters = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res = 0
        for i in range(n):
            if i < n - 1 and letters[s[i]] < letters[s[i + 1]]:
                res -= letters[s[i]]
            else:
                res += letters[s[i]]
        return res            