class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        stot = {}
        ttos = {}
        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]
            if char_s in stot:
                if stot[char_s] != char_t:
                    return False
            else:
                stot[char_s] = char_t
            if char_t in ttos:
                if ttos[char_t] != char_s:
                    return False
            else:
                ttos[char_t] = char_s            

        return True       



        