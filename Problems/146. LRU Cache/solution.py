class Node:
    
    def __init__(self, key, value):
        self.value = value
        self.prev = None
        self.next = None
        self.key = key


class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = {}
        self.history = None
        self.lru = None

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # if key is in cache edge cases:
        # - cache only has one element
        if (len(self.cache) > 1) and (self.cache[key] != self.history):
        # - accessed element is the tail (lru)
            if self.cache[key] == self.lru:
                self.cache[key].prev.next = None
                self.lru = self.cache[key].prev
                self.cache[key].next = self.history
                self.history.prev = self.cache[key]
                self.cache[key].prev = None
                self.history = self.cache[key]
        # - accessed element is the head (history)
        # - accessed element is in the middle of the list
            else:
                self.cache[key].prev.next = self.cache[key].next
                self.cache[key].next.prev = self.cache[key].prev
                self.cache[key].next = self.history
                self.history.prev = self.cache[key]
                self.history = self.cache[key]
        
        # at the end, return cache[key].value
        return self.cache[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # update
            self.cache[key].value = value
            # update history edge cases:
            # 1. there's only one element in the cache
            # 2. there's more than one element in the cache
            if len(self.cache) > 1:
                # 2.1. updated element is the head (history)
                if self.cache[key] == self.history:
                    return
                # 2.2. updated element is the tail (lru)
                if self.cache[key] == self.lru:
                    self.cache[key].prev.next = None
                    self.lru = self.cache[key].prev
                    self.cache[key].next = self.history
                    self.history.prev = self.cache[key]
                    self.cache[key].prev = None
                    self.history = self.cache[key]
                # 2.2. updated element is in the middle of the list
                else:
                    self.cache[key].prev.next = self.cache[key].next
                    self.cache[key].next.prev = self.cache[key].prev
                    self.cache[key].next = self.history
                    self.history.prev = self.cache[key]
                    self.cache[key].prev = None
                    self.history = self.cache[key]
        else:
            # insert new
            # steps:
            # - create Node
            newNode = Node(key, value)
            # - if history is empty:
            if self.history == None:
                # - make history and lru equal to Node.
                self.history = newNode
                self.lru = newNode
            # - if history is not empty:
            else:
                # - make Node.next equal to history
                newNode.next = self.history
                # - make history.prev equal to Node
                self.history.prev = newNode
                # - make history be equal to Node
                self.history = newNode
            # - insert into map (self.cache)
            self.cache[key] = newNode

            if len(self.cache) > self.size:
                # evict
                self.cache.pop(self.lru.key)
                self.lru.prev.next = None
                self.lru = self.lru.prev


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# capacity = 3
# currSize = 0
# 
# history = 8 <-> 9 <-> 4 <-> None
# lruCache =  { 1:->8, 2:->4, 5:->9 }

# Time complexity: O(1)
# Space complexity: O(n)
# Pattern: Linked Lists
# Time used: like 5 hours? LOL






