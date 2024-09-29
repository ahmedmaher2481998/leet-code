class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        c = 0
        jewel_set = set(jewels)
 
        for s in stones:
            if s in jewel_set:
                c += 1 
        return c

        