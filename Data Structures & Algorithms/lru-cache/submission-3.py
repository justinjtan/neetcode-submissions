class Node:
    def __init__(self, val=-1, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.caches = {}
        self.size = 0
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        cache = self.caches.get(key, -1)
        if cache == -1:
            return -1
        node = cache[1]
        self.update(node)
        return cache[0]

    def put(self, key: int, value: int) -> None:
        if key in self.caches:
            node = self.caches[key][1]
        else:
            node = Node(key, self.tail, None)
            self.size += 1
        self.caches[key] = (value, node)
        self.update(node)
        if self.size > self.capacity:
            LRU_key = self.head.val
            self.caches.pop(LRU_key)
            self.head = self.head.next
            self.size -= 1
        
    def update(self, node: Node) -> None:
        if not self.head:
            self.head = node
        if not self.tail:
            self.tail = node
        if node == self.tail:
            return
        elif node == self.head:
            self.head = node.next
            node.next.prev = None
        else:
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
        if self.tail:
            self.tail.next = node
        node.prev = self.tail
        node.next = None
        self.tail = node
