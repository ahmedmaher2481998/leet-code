class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        map = {c: i + 1 for i, c in enumerate(order)}
        print(map)
        # loop over worlds find first diff char if next is not greater returen false
        # if first word finished before second word with no diif cha detected return true

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            for j in range(len(w1)):
                if len(w2) == j:
                    return False
                if w1[j] != w2[j]:
                    if map[w1[j]] > map[w2[j]]:
                        return False
                    break
        return True
