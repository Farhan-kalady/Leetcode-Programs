class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for ch in s:
            if ch == "(" or ch == "{" or ch == "[":
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                bracket = stack.pop()
                if ((ch == ")" and bracket == "(") or (ch == "}" and bracket == "{") or (ch == "]" and bracket == "[")):
                    continue
                else:
                    return False
        return len(stack) == 0                   

