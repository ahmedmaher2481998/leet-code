from collections import defaultdict

class Solution:
    def fourSumCount(
        self, n1: List[int], n2: List[int], n3: List[int], n4: List[int]
    ) -> int:
        map = defaultdict(int)
        for i in n1:
            for j in n2:
                map[i +j] += 1
        count = 0
        for k in n3:
            for l in n4:
                count += map[-(l +k)]
        return count
