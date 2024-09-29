class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        chars = set()
        l = 0
        for r in range(len(s)):
            # if current char in list remove from l to current char
            # then update l
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            res = max(r - l + 1, res)
        return res 
