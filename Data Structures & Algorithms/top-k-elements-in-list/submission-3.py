class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #data structure in which the elements are ordered somehow by frequency, and then pop the k top elements

        #create a counter
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        #convert counter to frequency list
        freq = [[] for i in range(len(nums) + 1)]
        for num, count in counter.items():
            freq[count].append(num)

        #pop top k items from frequency list

        res = []


        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
            
