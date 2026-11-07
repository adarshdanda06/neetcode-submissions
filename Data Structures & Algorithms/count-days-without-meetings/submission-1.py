class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        mergedMeetings = []

        for meeting in meetings:
            if len(mergedMeetings) == 0 or mergedMeetings[-1][1] < meeting[0]:
                mergedMeetings.append(meeting)
            else:
                if meeting[1] > mergedMeetings[-1][1]:
                    mergedMeetings[-1][1] = meeting[1]

        res = 0
        for meeting in mergedMeetings:
            res += (meeting[1] - meeting[0] + 1)

        return days - res