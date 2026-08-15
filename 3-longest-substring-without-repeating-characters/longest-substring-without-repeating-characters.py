class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        my_dict = {}
        maxi = 0
        while right < len(s):
            if s[right] in my_dict:
                left = max(left, my_dict[s[right]] + 1 )

            maxi = max(maxi, right - left + 1)
            my_dict[s[right]] = right
            right += 1
        return maxi         