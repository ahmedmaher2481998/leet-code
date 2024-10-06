class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        r = 0
        for i in nums:
            r ^= i 
        for i in range(len(nums) + 1):
            r ^= i

        return r
