class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []

        result.append(intervals[0])
        for current in intervals[1:]:
            if current[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], current[1])
            else:
                result.append(current)
        return result            