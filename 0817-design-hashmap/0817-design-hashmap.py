class NodeList:
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.next = None


class MyHashMap:

    def __init__(self):
        self.map = [NodeList(-1, -1) for _ in range(1000)]

    def hash(self, key: int) -> int:
        index = key % len(self.map)
        return index

    def put(self, key: int, value: int) -> None:
        index = self.hash(key)  # dummy node
        head = self.map[index]
        while head.next:
            if head.next.key == key:
                head.next.value = value
                return
            head = head.next
        head.next = NodeList(key, value)

    def get(self, key: int) -> int:
        index = self.hash(key)
        head = self.map[index].next
        while head:
            if head.key == key:
                return head.value
            head = head.next
        return -1

    def remove(self, key: int) -> None:
        index = self.hash(key)
        head = self.map[index]
        prev = head
        head = head.next

        while head:
            if head.key == key:
                prev.next = head.next
            prev = head
            head = head.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
