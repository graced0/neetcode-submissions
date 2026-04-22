class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        result = [intervals[0]]
        for start, end in intervals[1:]:
            prevEnd = result[-1][1]
            if start <= prevEnd: #merge them
                result[-1][1] = max(end, prevEnd)
            else: # append without merging
                result.append([start, end])
        return result
