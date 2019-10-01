class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        if not len(intervals):
            return 0
        intervals.sort()
        rooms = []

        for interval in intervals:
            to_append = False
            for room in rooms:
                if interval[0] >= room[1]:
                    room[1] = interval[1]
                    to_append = False
                    break
                to_append = True
            if to_append or not len(rooms):
                rooms.append(interval)





        return len(rooms)
