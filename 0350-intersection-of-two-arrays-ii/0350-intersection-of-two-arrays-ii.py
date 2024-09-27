class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        n1 , n2 = nums1 , nums2
        for i in n1:
            if i in n1 and i in n2:
                # n1.remove(i)
                n2.remove(i)
                res.append(i)
        return res
        