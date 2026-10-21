class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = [intervals[0]]
        for i in range(1, len(intervals)):
            if merged[-1][1] >= intervals[i][0]: #if there is an overlap
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
            else: #if there is no overlap
                merged.append(intervals[i])

        return merged