from collections import defaultdict


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        map = {}
        for i in arr:
            map[i] = (map[i] + 1)  if i in map else 1 
        return len(map.keys()) == len(set(map.values()))
