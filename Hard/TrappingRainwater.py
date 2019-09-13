class Solution:
    def trap(self, height: List[int]) -> int:

        left = []
        right = []
        cur = 0
        for i in range(len(height)):
            if height[i] > cur:
                cur = height[i]

            left.append(cur)


        cur = 0
        for i in range(1, len(height) + 1):
            if height[-i] > cur:
                cur = height[-i]

            right.append(cur)

        right = right[::-1]
        print(left)
        print(right)
        sum = 0
        for i in range(len(height)):
            sum += min(right[i], left[i]) - height[i]

        return sum


# Runtime: 60 ms, faster than 74.70% of Python3 online submissions for Trapping Rain Water.
# Memory Usage: 14.6 MB, less than 6.98% of Python3 online submissions for Trapping Rain Water.
