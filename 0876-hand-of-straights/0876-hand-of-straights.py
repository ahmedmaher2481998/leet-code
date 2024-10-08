class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        h = list(set(hand)) # to trak elements only 
        heapq.heapify(h)
        map = {} 
        # to track frequecny of each element 
        for i in hand:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1
        res = []
        while len(h) != 0:
            i = h[0] # min element 
            if map[i] != 0:
                map[i] -= 1
                t = [i]
                for j in range(1, groupSize):
                    new = i  +j 
                    if new in map and map[new] != 0:
                        map[new] -= 1
                        t.append(new)
                    else:
                        return False
            else:
                heapq.heappop(h)
        return True
