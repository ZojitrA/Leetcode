class Solution:
    def rob(self, nums: List[int]) -> int:

        for i in range(2, len(nums)):
            if nums[i - 2] + nums[i] > nums[i -1]:
                nums[i] = nums[i-2] + nums[i]
            nums[i - 1] = max(nums[i - 2], nums[i-1])


        try:
            return max(nums[-1], nums[-2])
        except:
            try:
                return nums[-1]
            except:
                return 0
