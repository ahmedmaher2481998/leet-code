# class Node:
#     def __init_(self,input):
#         key , value =  input
#         self.value = value
#         self.key = key
#         self.next = None

class MyHashMap:

    def __init__(self):
        self.map = [[] for _ in range(10**6)]

    def hash(self,key:int)-> int:
        index = key % len(self.map)
        return index
        

    def put(self, key: int, value: int) -> None:
        index = self.hash(key)
        self.map[index] = [key,value]
        

    def get(self, key: int) -> int:
        index = self.hash(key)
        if len(self.map[index]) != 0:
            return self.map[index][-1]
        else:
            return -1

    def remove(self, key: int) -> None:
        index = self.hash(key)
        if len(self.map[index]) != 0:
            self.map[index] = []


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)