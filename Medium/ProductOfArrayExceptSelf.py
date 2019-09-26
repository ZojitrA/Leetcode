class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [1 for el in nums] + [1]
        r = [1 for el in nums] + [1]
        for i in range(len(nums)):
            l[i+1] = l[i] * nums[i]
            r[-i-2] = r[-i - 1] * nums[-i -1]

        l = l[1:]
        r = r[:-1]
        for i in range(len(nums)):
            if i-1 >= 0 and i+1 < len(nums):
                nums[i] = l[i-1] * r[i+1]
            elif i-1 >= 0:
                nums[i] = l[i-1] * 1
            elif i+1 < len(nums):
                nums[i] = 1*r[i+1]
            else:
                nums[i] = 1
        return nums

# has to be O(n) runtime without using division
# Runtime: 152 ms, faster than 19.38% of Python3 online submissions for Product of Array Except Self.
# Memory Usage: 19.9 MB, less than 94.00% of Python3 online submissions for Product of Array Except Self.
