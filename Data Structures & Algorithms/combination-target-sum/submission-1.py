class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(target, start, combos):
            if target == 0:
                res.append(list(combos))
                return
            if target < 0:
                return
            for i in range(start, len(nums)):
                combos.append(nums[i])
                backtrack(target - nums[i], i, combos)
                combos.pop()

        backtrack(target, 0, [])
        return res