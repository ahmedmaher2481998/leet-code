import heapq


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        result = []
        # if len(nums1) < k or len(nums2) < k:
        #     return result

        seen = set()
        heap = []
        sum = nums1[0] + nums2[0]
        heapq.heappush(heap, (sum, 0, 0))
        seen.add((0, 0))
        while k and heap:
            _, i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])
            # is there's next for i and not seen
            if i + 1 < len(nums1) and (i + 1, j) not in seen:
                seen.add((i + 1, j))
                sum = nums1[i + 1] + nums2[j]
                heapq.heappush(heap, (sum, i + 1, j))
            # is there's next for j and not seen
            if j + 1 < len(nums2) and (i, 1 + j) not in seen:
                seen.add((i, 1 + j))
                sum = nums1[i] + nums2[1 + j]
                heapq.heappush(heap, (sum, i, 1 + j))
            k -= 1
        return result
