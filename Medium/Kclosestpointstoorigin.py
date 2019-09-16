class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        return self.pointSort(points, K)[:K]

    def pointSort(self, points, K):
        if len(points) < 2:
            return points

        left = []
        right = []
        mid = []
        pivot = points[len(points)//2]
        pivotdis = self.distanceish(pivot)

        while len(points):
            current = points.pop()
            curdis = self.distanceish(current)
            if curdis > pivotdis:
                right.append(current)
            elif curdis < pivotdis:
                left.append(current)
            else:
                mid.append(current)

        if len(left) >= K:
            return self.pointSort(left, K)
        elif len(left) + len(mid) >= K:
            return self.pointSort(left, K) + mid
        else:
            return self.pointSort(left, K) + mid + self.pointSort(right, K)


    def distanceish(self, point):
        return (point[0]**2 + point[1]**2)
