class Solution:
    def fib(self, n: int,map={}) -> int:
        if n == 1:
            return 1
        elif n <= 0  :
            return 0
        else:
            left = 0
            right = 0
            if n -1 in map:
                left = map[n -1]
            else:
                left = map[n - 1] = self.fib(n - 1 ,map)
            if n -2 in map:
                right = map[n -2]
            else:
                right = map[n - 2 ] = self.fib(n - 2 ,map)
        return  map[n - 1] + map[n - 2]