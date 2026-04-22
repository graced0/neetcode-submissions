class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        window = []
        q = deque()
        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()    
            q.append(r)
            if q[0] < l:
                q.popleft()
            if r + 1 >= k:
                window.append(nums[q[0]])
                l+=1

        return window