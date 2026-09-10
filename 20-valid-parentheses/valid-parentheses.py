class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
            if i == "(" or i == "{" or i == "[":
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                
                bucket = stack.pop()
                if ((i == ")" and bucket == "(") or (i == "}" and bucket == "{") or (i == "]" and bucket == "[")):
                    continue
                else:
                    return False
        return len(stack) == 0                                             

