class MyHashSet:

    def __init__(self):
        self.data = [[]] * 10

    def hash(self,key: int) -> int:
        return key % 10

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        else:
            list = self.data[self.hash(key)]
            list.append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            list = self.data[self.hash(key)]
            # index = list.index(key)
            list.remove(key)
            return True
        else:
            return False

    def contains(self, key: int) -> bool:
        index = self.hash(key)
        list = self.data[index]
        if len(list):
            return key in list
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
