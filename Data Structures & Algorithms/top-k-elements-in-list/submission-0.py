class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0)

        freq = [[] for i in range(len(nums) + 1)]
        for num, count in hashmap.items():
            freq[count].append(num)

        result = []
        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
        return []