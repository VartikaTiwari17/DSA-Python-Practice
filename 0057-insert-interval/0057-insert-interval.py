class Solution:
    def insert(self, intervals, newInterval):
        result = []
        i = 0
        n = len(intervals)

        # Jo intervals newInterval se pehle hain
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # Overlapping intervals ko merge karo
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        # Merged newInterval
        result.append(newInterval)

        # Baaki intervals
        while i < n:
            result.append(intervals[i])
            i += 1

        return result