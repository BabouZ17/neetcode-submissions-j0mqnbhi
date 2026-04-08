"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        starts = [i.start for i in intervals]
        starts.sort()
        ends = [i.end for i in intervals]
        ends.sort()

        i = j = 0
        cnt = res = 0
        while i < len(starts):
            if starts[i] < ends[j]:
                cnt += 1
                i += 1
            else:
                j += 1
                cnt -= 1
            res = max(res, cnt)
        return res