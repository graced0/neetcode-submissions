class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #i want a hash map to record key value pairs
        #i should be able to check for a previously seen value and and get its indice

        #k:v -> num:indice
        seen = {}

        for curr_index in range(len(nums)):
            if target - nums[curr_index] in seen:
                return [seen[target - nums[curr_index]], curr_index]
            else:
                seen[nums[curr_index]] = curr_index

        
