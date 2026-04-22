class Solution:
    def findMin(self, nums: List[int]) -> int:
        result = nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] < nums[r]: # edge case if already sorted
                result = min(result, nums[l])
                return result
            m = (l + r) // 2
            result = min(result, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1 #exclude middle as we already checked for min
            else:
                r = m - 1 #exclude middle as we already checked for min
        return result
        