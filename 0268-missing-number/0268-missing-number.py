class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = 0 
        while n in nums:
            n += 1
        return n 
        