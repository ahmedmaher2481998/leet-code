# from collections import heapq


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        h = list(set(hand))
        heapq.heapify(h)
        # print(h)
        map = {}
        for i in hand:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1
        res = []
        while len(h) != 0:
            i = h[0]
            if map[i] != 0:
                t = [i]
                map[i] -= 1
                for j in range(1, groupSize):
                    new = i  +j 
                    if new in map and map[new] != 0:
                        map[new] -= 1
                        t.append(new)
                    else:
                        return False
                    # print(f"j {j}")
            else:
                heapq.heappop(h)
        return True
