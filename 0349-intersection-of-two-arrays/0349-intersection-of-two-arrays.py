class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set()
        if len(nums1) <= len(nums2):
            shorter = nums1
            longer = nums2
        else:
            shorter = nums2
            longer = nums1

        for i in range(len(shorter)):

            if shorter[i] in nums1 and shorter[i] in nums2 :
                seen.add(shorter[i])
        return list(seen)
        