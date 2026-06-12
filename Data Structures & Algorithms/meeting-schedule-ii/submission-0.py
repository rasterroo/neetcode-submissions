"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        output = 0
        rooms = 0
        events = []
        
        for interval in intervals:
            events.append((interval.start, 1))
            events.append((interval.end, -1))
        
        events.sort(key=lambda x: (x[0], x[1]))
        for event in events:
            rooms += event[1]
            output = max(output, rooms)

        return output