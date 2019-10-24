class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not len(nums):
            return 0

        dtable = [1 for el in nums]

        for i in range(len(dtable)):

            for j in range(0, i):
                if nums[j] < nums[i]:
                    if dtable[j] >= dtable[i]:
                        dtable[i] = 1 + dtable[j]

        return max(dtable)
