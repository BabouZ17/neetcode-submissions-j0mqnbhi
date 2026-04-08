"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts, ends = sorted([val.start for val in intervals]), sorted([val.end for val in intervals])
        l, r = 0, 0
        count, maxCount = 0, 0
        
        while l < len(intervals):
            if starts[l] < ends[r]:
                count += 1
                l += 1
            else:
                count -= 1
                r += 1
            maxCount = max(maxCount, count)
        return maxCount