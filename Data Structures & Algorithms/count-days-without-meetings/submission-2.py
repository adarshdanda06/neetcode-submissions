class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        lastEnd = 0
        ans = days

        for meeting in meetings:
            start = meeting[0]
            end = meeting[1]

            if start > lastEnd:
                ans -= end - start + 1
            elif end > lastEnd:
                ans -= end - lastEnd
            else:
                continue

            lastEnd = end

        return ans