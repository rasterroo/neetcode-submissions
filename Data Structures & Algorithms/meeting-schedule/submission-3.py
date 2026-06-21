"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # intuition. sort array by start time. then, compare curr interval with prev for each interval
        # if current start time is strictly less than the prev end time, then return False. Else, keep going
        if len(intervals)<=1:
            return True

        intervals.sort(key = lambda x: x.start)
        prev = intervals[0]

        for curr in intervals[1:]:
            if curr.start < prev.end:
                return False
            prev = curr

        return True