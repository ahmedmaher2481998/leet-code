class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Create a hashmap to store the frequency of elements in nums1
        count_map = {}
        for num in nums1:
            if num in count_map:
                count_map[num] += 1
            else:
                count_map[num] = 1

        result = []

        # Traverse nums2 and check if the element is in the hashmap
        for num in nums2:
            if num in count_map and count_map[num] > 0:
                result.append(num)
                count_map[num] -= 1

        return result
        