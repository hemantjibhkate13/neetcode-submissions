class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(s) < len(t):
            return ""

        target_count = {}
        for ch in t:
            if ch in target_count:
                target_count[ch] += 1
            else:
                target_count[ch] = 1

        required = len(target_count)
        formed = 0

        window_count = {}
        left = 0
        best_len = float("inf")
        best_start = 0

        for right in range(len(s)):
            add_char = s[right]
            if add_char in window_count:
                window_count[add_char] += 1
            else:
                window_count[add_char] = 1

            if add_char in target_count and window_count[add_char] == target_count[add_char]:
                formed += 1

            while left <= right and formed == required:
                curr_len = right - left + 1
                if curr_len < best_len:
                    best_len = curr_len
                    best_start = left

                remove_char = s[left]
                window_count[remove_char] -= 1

                if remove_char in target_count and window_count[remove_char] < target_count[remove_char]:
                    formed -= 1

                left += 1

        if best_len == float("inf"):
            return ""

        return s[best_start : best_start + best_len]