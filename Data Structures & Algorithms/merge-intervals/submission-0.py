class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            
            if start <= merged[-1][1]:
                merged[-1] = [merged[-1][0], max(end, merged[-1][1])]
            else:
                merged.append([start, end])

        return merged