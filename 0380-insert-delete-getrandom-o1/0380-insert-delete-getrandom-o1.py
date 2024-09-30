import random
from collections import defaultdict
class RandomizedSet:

    def __init__(self):
        self.s = []
        self.map = defaultdict(int)
    
    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.map[val] = len(self.s) 
        self.s.append(val)
        return True
        
    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        # print('s',self.s,self.map)
        # local val in s
        i = self.map[val]
        # swap val with last index 
        temp = self.s[i]
        last = self.s[-1]
        self.s[i] = last
        #last index changed change it's index 
        self.map[self.s.pop()] = self.map[val]
        del self.map[val]
        # print(f's : { self.s} after deleting {val}')
        return True

    def getRandom(self) -> int:
        s = random.choice(self.s)
        # print(self.s,s)
        return s

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()