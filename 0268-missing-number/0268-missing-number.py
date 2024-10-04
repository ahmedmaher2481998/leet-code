class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_set = set(nums)
        n = len(nums)
        
        # Check all numbers from 0 to n
        for i in range(n + 1):
            if i not in num_set:
                return i