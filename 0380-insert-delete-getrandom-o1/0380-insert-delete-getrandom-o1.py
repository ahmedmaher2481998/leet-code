import random
class RandomizedSet:

    def __init__(self):
        self.s = set()
    

    def insert(self, val: int) -> bool:
        if val in self.s:
            return False
        self.s.add(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val in self.s:
            self.s.remove(val)
            return True
        return False

        

    def getRandom(self) -> int:
        if len(self.s) > 0:
            i = int(random.random() * len(self.s))
            return list(self.s)[i]

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()