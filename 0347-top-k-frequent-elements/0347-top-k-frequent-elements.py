from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict()
        for i in nums:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1
        # print(map) #return form top freq to k freq 
        vals = list(map.values()) 
        vals.sort()
        vals = vals[len(map) - k :]
        res=[]
        for v in vals:
            k = list(map.keys())[(list(map.values()).index(v))]
            res.append(k)
            del map[k]
            # print('key is',k)
        return res 