class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            speed = left + (right - left) // 2

            # Step 1: Calculate total hours using a normal loop
            hours = 0

            for p in piles:
                pile_hours = p // speed

                if p % speed != 0:
                    pile_hours += 1

                hours += pile_hours

            # Step 2: Decide whether this speed is sufficient
            if hours <= h:
                right = speed
            else:
                left = speed + 1

        return left