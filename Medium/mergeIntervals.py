class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        def merge(intz):

            for i in range(len(intz) - 1):
                if intz[i][1] >= intz[i+1][0]:
                    intz[i+1][0] = intz[i][0]
                    intz[i+1][1] = max(intz[i][1], intz[i+1][1])
                    intz = intz[0:i] + intz[i+1:]
                    intz = merge(intz)
                    break

            return intz

        return merge(intervals)
                
