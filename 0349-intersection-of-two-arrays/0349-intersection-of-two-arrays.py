class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_set = set(nums1)
        result =[]
        for i in hash_set:
            if i in nums2:
                result.append(i)
        return result 

        