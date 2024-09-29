from collections import defaultdict
class Solution:
    def fourSumCount(self, n1: List[int], n2: List[int], n3: List[int], n4: List[int]) -> int:
        map = {}
        for i in n1:
            for j in n2:
                sum = i +j 
                if sum in map:
                    map[sum] += 1
                else:
                    map[sum] = 1
        count = 0
        for k in n3:
            for l in n4:
                sum = - (k +l)
                if  sum in map:
                    count += map[sum] 
                
        return count 
        