class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        nums2_set = set(nums2)
        for num in nums1:
            if num in nums2_set and num not in res:
                    res.append(num)
        return res