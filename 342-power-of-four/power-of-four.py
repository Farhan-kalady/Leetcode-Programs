class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        if n>0 and (n & n - 1 == 0) and ((n & 0xAAAAAAAA) == 0):
            return True
        else :
            return False  
        