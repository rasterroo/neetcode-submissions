class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.nxt = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}  # {key : Node}
        self.capacity = capacity
        self.tail, self.head = Node(0, 0), Node(0, 0)
        self.tail.nxt, self.head.prev = self.head, self.tail

    def insert(self, node):
        # a <-> head
        # a <-> b <-> head
        prev, nxt = self.head.prev, self.head
        prev.nxt = nxt.prev = node
        node.nxt, node.prev = nxt, prev
        
    def remove(self, node):
        prev, nxt = node.prev, node.nxt
        prev.nxt, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            LRU = self.tail.nxt 
            self.remove(LRU)
            del self.cache[LRU.key]

