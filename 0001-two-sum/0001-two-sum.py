class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans={}
        for i in range(len(nums)):
            second_element = target - nums[i]
            if second_element in ans:
                return [ans[second_element],i]
            else:
                ans[nums[i]] = i
        