class Solution:
    def minTimeToVisitAllPoints(self, points):
        if len(points) == 1:
            return 0
        else:
            seconds = 0
            for i in range(len(points)-1):
                start = points[i]
                end = points[i+1]
                minimum = min(abs(start[0] - end[0]), abs(start[1] - end[1]))
                seconds += minimum
                seconds += max(abs(start[0] - end[0]), abs(start[1] - end[1])) - minimum
            return seconds
