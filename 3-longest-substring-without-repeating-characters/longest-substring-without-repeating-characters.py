class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Dictionary to store the last seen index of each character
        last_seen = {}
        start = 0
        max_length = 0
        
        for end, char in enumerate(s):
            # If the character is already in our dictionary and its last seen index 
            # is inside our current sliding window, move the start pointer past it.
            if char in last_seen and last_seen[char] >= start:
                start = last_seen[char] + 1
            
            # Update the last seen index of the character
            last_seen[char] = end
            
            # Calculate the current window size and update max_length if it's larger
            max_length = max(max_length, end - start + 1)
            
        return max_length