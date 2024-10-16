class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        count = Counter(tasks)
        res = 0 
        for c in count.values():
            if c == 1:
                return -1 
            res += c // 3
            if c % 3 > 0 :
                res += 1 
            # print(c // 3 , c)
        # print(count)
        return res
        