class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map = {}
        for i,n in enumerate(nums):
            if n in map:
                res = abs(map[n] - i)
                if res <= k:
                    return True 
                else:
                    map[n] = i 
            else:
                map[n] = i
        return False

        