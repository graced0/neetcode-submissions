class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #top # most frequent indicates we need a max heap
        #we also need a counter to determine frequency for each num

        #create a counter
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        #flip counter where count is the index in a list, and the corresponding number is the value
        freq = [[] for i in range (len(nums) + 1)]
        for num, count in counter.items():
            freq[count].append(num)

        #go through the freqency list, largest value to smallest value (aka highest freq to lowest)
        res = []
        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k: #append corresponding high freq value into res until k values
                    return res
        
        return res