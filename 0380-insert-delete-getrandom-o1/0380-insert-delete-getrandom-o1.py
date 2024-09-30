import random
class RandomizedSet:

    def __init__(self):
        self.s = []
        self.map = {}
    
    def insert(self, val: int) -> bool:
        if val in self.s:
            return False
        self.s.append(val)
        self.map[val] = len(self.s) - 1 
        return True
        
    def remove(self, val: int) -> bool:
        if val in self.s:
            self.s.remove(val)        
            del self.map[val]
            return True
        return False

        

    def getRandom(self) -> int:
        return random.choice(self.s)

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()