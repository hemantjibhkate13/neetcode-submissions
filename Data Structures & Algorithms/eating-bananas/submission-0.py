class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            speed = left + (right - left) // 2
            hours = sum((p + speed - 1) // speed for p in piles)  # ceil(p / speed)
            if hours <= h:
                right = speed
            else:
                left = speed + 1
        return left

        