class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # Mid is on the higher left portion; minimum must be to the right of mid
            if nums[mid] > nums[right]:
                left = mid + 1
            # Mid is on the lower/sorted portion (or equals it); minimum is at mid or to its left
            else:
                right = mid

        return nums[left]