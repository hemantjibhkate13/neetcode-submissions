class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res_s = {}
        res_t = {}

        for char in s:
            if char in res_s:
                res_s[char] += 1
            else:
                res_s[char] = 1

        for char in t:
            if char in res_t:
                res_t[char] += 1
            else:
                res_t[char] = 1
        
        if res_s == res_t:
            return True
        else:
            return False
        