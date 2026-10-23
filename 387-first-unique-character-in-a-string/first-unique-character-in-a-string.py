class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_freq = {}
        for ch in s:
            char_freq[ch] = char_freq.get(ch, 0) + 1
        for i in range(len(s)):
            if char_freq[s[i]] == 1:
                return i
        return -1        
