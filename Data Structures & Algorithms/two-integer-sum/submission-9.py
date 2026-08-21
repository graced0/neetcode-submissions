class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #i should be able to check for a previously seen value and and get its indice
        #k:v -> num:indice
        
        seen = {}

        for i, n in enumerate(nums):
            if target - n in seen:
                return [seen[target - n], i] #return the answer with the smaller index first.
            seen[n] = i

        
        
