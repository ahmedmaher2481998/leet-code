class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # s = set()
        # for i in nums:
        #     if i not in s:
        #         s.add(i)
        #     else:
        #         return i
        # floyed alogrthim 
        # i just learn it 
        # first make fast & slow intercest 
        # then make new slow and use it to make it intersect with the old slow 
        # when they intersect , it's  the duplicatye number 
        fast , slow = 0, 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if slow == fast :
                break 
        slow2 = 0 

        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2 :
                return slow2
