"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        for j in range(0, len(intervals)):
            start = intervals[j].start
            end = intervals[j].end

            for i in range(j + 1, len(intervals)):
                if intervals[i].end > start and intervals[i].end < end:
                    return False
                elif intervals[i].start > start and intervals[i].start < end:
                    return False


        return True