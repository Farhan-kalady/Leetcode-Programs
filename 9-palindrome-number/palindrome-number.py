class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num = x
        rev = 0

        while num > 0:
            rev = rev * 10 + num % 10
            num = num // 10
        return rev == x          