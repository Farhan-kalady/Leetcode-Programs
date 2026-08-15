class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       hash_s = {}
       hash_t = {}
       for ch in s:
        hash_s[ch] = hash_s.get(ch, 0) + 1
       for ch in t:
        hash_t[ch] = hash_t.get(ch, 0) + 1
       return hash_s == hash_t  
