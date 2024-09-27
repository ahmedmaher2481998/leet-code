class Solution:
    def firstUniqChar(self, s: str) -> int:
        map = {}
        for i, char in enumerate(s):
            if char in map:
                map[char] = -1
            else:
                map[char] = i
        for i in map:
            if map[i] != -1:
                return map[i]
        return -1 