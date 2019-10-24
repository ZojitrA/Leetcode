class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True

        cur_jump = nums[0]
        i = 0
        while cur_jump > 0:

            cur_jump -= 1
            i+=1

            if i == len(nums) - 1:
                return True


            if nums[i] > cur_jump:
                cur_jump = nums[i]

        return False
