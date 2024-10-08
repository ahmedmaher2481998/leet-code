class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # Three's a beter solution using Sets
        # l,r=0,10
        # map={}
        # if len(s) < 10:
        #     return []
        # while r  <= len(s):
        #     sub = s[l:r]
        #     if sub in map:
        #         map[sub] += 1
        #     else:
        #         map[sub] = 1
        #     l += 1 
        #     r += 1
        # res = []
        # return [key for key,value in map.items() if value > 1]
        seen = set()
        res = set()
        for i in range(len(s) - 9):
            sub = s[i:i+10]
            if sub in seen:
                res.add(sub)
            else:
                seen.add(sub)
        return list(res)