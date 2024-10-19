class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            second = target - nums[i]
            if second in map:
                return [map[second],i]
            else:
                map[nums[i]] = i 
        return []
