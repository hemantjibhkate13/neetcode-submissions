class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        state = {}
        max_length = 0
        start = 0

        for end in range(len(s)):

            current_char = s[end]

            # Add the current character to the dictionary
            if current_char in state:
                state[current_char] += 1
            else:
                state[current_char] = 1

            # Remove characters from the left until
            # the current window has no duplicate
            while state[current_char] > 1:

                left_char = s[start]

                state[left_char] -= 1

                start += 1

            # Current window is now valid
            current_length = end - start + 1

            if current_length > max_length:
                max_length = current_length

        return max_length