class Solution:
    def fib(self, n: int, map={}) -> int:
        # Solving using tabulation / bottoum up
        if n == 0:
            return 0 
        if n == 1:
            return 1 

        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1]
        # print(dp)
        return dp[n]
        # if n == 1:
        #     return 1
        # elif n <= 0  :
        #     return 0
        # else:
        #     left = 0
        #     right = 0
        #     if n -1 in map:
        #         left = map[n -1]
        #     else:
        #         left = map[n - 1] = self.fib(n - 1 ,map)
        #     if n -2 in map:
        #         right = map[n -2]
        #     else:
        #         right = map[n - 2 ] = self.fib(n - 2 ,map)
        # return  map[n - 1] + map[n - 2]
