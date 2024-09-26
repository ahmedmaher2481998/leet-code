class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans = {}
        if len(list1) > len(list2):
            shortList = list2
            longList = list1
        else:
            shortList = list1
            longList = list2
        # getting common with smallest indexies
        for i in range(len(shortList)):
            # element from the shortList array
            el = shortList[i]
            if el in longList:  # if ture we found a common
                sum = longList.index(el) + i
                if sum in ans:
                    ans[sum].append(el)
                else:
                    ans[sum] = [el]
        smallest = float("inf")
        for i in ans:
            if int(i) < smallest:
                smallest = i
        return ans[smallest]
