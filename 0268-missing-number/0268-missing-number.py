class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        while n in nums and n >= 0 :
            n -= 1
        return n 
        