from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        result = []

        for right in range(len(nums)):
            # 1. Remove indices that are now outside the window [right - k + 1, right]
            left_bound = right - k + 1
            while len(dq) > 0 and dq[0] < left_bound:
                dq.popleft()

            # 2. Maintain monotonic decreasing values: pop smaller elements from the back
            while len(dq) > 0 and nums[dq[-1]] <= nums[right]:
                dq.pop()

            # 3. Add current index
            dq.append(right)

            # 4. Record maximum once the first full window of size k is formed
            if right >= k - 1:
                max_val = nums[dq[0]]
                result.append(max_val)

        return result