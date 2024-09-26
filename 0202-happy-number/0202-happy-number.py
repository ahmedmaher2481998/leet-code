class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        res = n 
        while res  not in seen:
            seen.add(res)
            newRes =  0
            for  i in list(str(res)):
                newRes += int(i) ** 2 
            res = newRes
        
        return res == 1
