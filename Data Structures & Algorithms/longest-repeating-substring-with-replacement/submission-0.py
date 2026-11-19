class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        state = {}
        max_freq = 0
        max_length = 0
        start = 0

        for end in range(len(s)):
            curr_char = s[end]
            if curr_char in state:
                state[curr_char] +=  1
            else:
                state[curr_char] = 1

            max_freq = max(max_freq, state[curr_char])
            curr_length = end - start + 1

            while curr_length - max_freq > k:
                left_char = s[start]
                state[left_char] -= 1
                start += 1
                curr_length = end - start + 1

            max_length = max(max_length, curr_length)

        return max_length
