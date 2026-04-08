"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = [i.start for i in intervals]
        starts.sort()
        ends = [i.end for i in intervals]
        ends.sort()

        i = j = 0
        count = res = 0
        while i < len(intervals):
            if starts[i] < ends[j]:
                i += 1
                count += 1
            else:
                j += 1
                count -= 1
            res = max(res, count)
        return res
