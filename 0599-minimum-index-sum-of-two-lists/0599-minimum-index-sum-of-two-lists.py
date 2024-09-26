class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list3 = [value for value in list1 if value in list2]
        map={}
        for i in list3:
            sum = list1.index(i) + list2.index(i) 
            if sum in map:
                map[sum].append(i)
            else:
                map[sum] = [i]
        key = list(map.keys())
        key.sort()
        return map[key[0]]
            