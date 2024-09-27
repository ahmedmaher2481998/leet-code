class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def hash(s:str)->str:
            a = list(s)
            print(a) 
            a.sort()
            return ''.join(a)
        map = {}
        for s in strs:
            key = hash(s)
            if key in map:
                map[key].append(s)
            else:
                map[key] = [s]
        return map.values()


        