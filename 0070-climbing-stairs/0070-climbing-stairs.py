class Solution:
    def climbStairs(self, n: int,map={}) -> int:
        
        # print(f'n is {n}')
        if(n <= 1):
            return 1
        if n in map:
            return map[n]
        else:
            map[n] = self.climbStairs(n-1,map) +  self.climbStairs(n-2,map)
            return map[n]
        

        