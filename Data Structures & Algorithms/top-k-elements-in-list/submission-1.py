class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #top # most frequent indicates we need a max heap
        #we also need a counter to determine frequency for each num

        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        heap = []
        for val, count in freq.items():
            heapq.heappush(heap, (-count, val))

        res = []
        for _ in range(k):
            count, val = heapq.heappop(heap)
            res.append(val)
        
        return res