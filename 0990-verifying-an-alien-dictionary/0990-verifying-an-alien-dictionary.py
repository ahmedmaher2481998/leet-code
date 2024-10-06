class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # first letter same?
        # continue
        # :different
        # next word first letter is latter in order than current word first letter
        # if this word is suffex of next word it's okay to be in front of it
        # so if next work is sufex it's okay it's wrong
        map = {c: i for i, c in enumerate(order)}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            # if w2 is suffex of w1 it's not valid
            for j in range(len(w1)):
                if len(w2) == j:
                    return False
                if w1[j] != w2[j]:
                    if map[w1[j]] > map[w2[j]]:
                        return False
                    break  # it's legit order no need to continue
        # print(map)

        return True
