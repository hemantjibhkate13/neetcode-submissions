class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)

        if len1 > len2:
            return False

        s1_count = {}
        for ch in s1:
            if ch in s1_count:
                s1_count[ch] += 1
            else:
                s1_count[ch] = 1

        window_count = {}
        for i in range(len1):
            ch = s2[i]
            if ch in window_count:
                window_count[ch] += 1
            else:
                window_count[ch] = 1

        if s1_count == window_count:
            return True

        for right in range(len1, len2):
            add_char = s2[right]
            if add_char in window_count:
                window_count[add_char] += 1
            else:
                window_count[add_char] = 1

            left_index = right - len1
            remove_char = s2[left_index]
            window_count[remove_char] -= 1
            if window_count[remove_char] == 0:
                del window_count[remove_char]

            if s1_count == window_count:
                return True

        return False