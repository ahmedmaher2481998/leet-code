class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map = {}
        for i in nums1:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1
        res = []
        for i in nums2:
            if i in map and map[i] > 0 :
                res.append(i)
                map[i] -= 1 
        return res  
        