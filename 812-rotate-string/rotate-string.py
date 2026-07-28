class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        double = s + s
        if goal in double :
            return True
        return False    