"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        res = [(item.start, item.end) for item in intervals]

        res.sort(key= lambda x: (x[0], x[1]))

        for i in range(1, len(res)):
            if res[i - 1][1] > res[i][0]:
                return False

        return True 