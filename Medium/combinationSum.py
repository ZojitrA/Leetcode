class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combos = []

        def recurz(targ, nums= [], start = 0):
            if targ == 0:
                combos.append(nums)
                return
            if targ < 0:
                return
            for i in range(start, len(candidates)):
                new_array = nums + [candidates[i]]
                recurz(targ - candidates[i], new_array, i)

        recurz(target, [])
        return combos

# Runtime: 88 ms, faster than 55.68% of Python3 online submissions for Combination Sum.
# Memory Usage: 13.7 MB, less than 6.06% of Python3 online submissions for Combination Sum.
