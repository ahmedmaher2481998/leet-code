class Node:
    def __init__(self, key: int):
        self.key = key
        self.next = None


class MyHashSet:

    def __init__(self):
        self.set = [Node(0) for _ in range(10**4)]

    def hash(self, key: int) -> Node:
        index = key % len(self.set)
        return self.set[index]

    def add(self, key: int) -> None:
        head = self.hash(key)
        while head.next is not None:
            if head.next.key == key:
                return
            else:
                head = head.next
        head.next = Node(key)
        return

    def remove(self, key: int) -> None:
        head =  self.hash(key).next
        prev = None
        while head:
            if head is None:
                return
            elif head.key == key:
                if prev is None:
                    index = self.hash(key)
                    index.next = head.next
                else:
                    prev.next = head.next
                return
            prev = head
            head = head.next
        

    def contains(self, key: int) -> bool:
        head = self.hash(key)
        head = head.next
        while head:
            if head.key == key:
                return True
            head = head.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
