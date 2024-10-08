class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        l,r=0,10
        map={}
        def hash(sub):
            return "".join(sub)
        if len(s) < 10:
            return []
        while r  <= len(s):
            sub = hash([s[l:r]])
            if sub in map:
                map[sub] += 1
            else:
                map[sub] = 1
            l += 1 
            r += 1
        res = []
        # print(map)
        return [key for key,value in map.items() if value > 1]


        