class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict() #last -> most recently used, first -> LRU
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key) #-> most recently used
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key) #-> most recently used
        self.cache[key] = value

        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)
        
