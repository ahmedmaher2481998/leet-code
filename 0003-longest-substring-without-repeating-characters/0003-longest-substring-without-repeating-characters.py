class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        res = 0
        start = 0
        main_max = 0
        map = set()
        i = 0
        while i < len(string):
            s = string[i]
            if s in map:
                start += 1
                i = start
                main_max = max(main_max, res)
                res = 0
                map.clear()
            else:
                map.add(s)
                res = res + 1
                i += 1

        return max(main_max, len(map))
