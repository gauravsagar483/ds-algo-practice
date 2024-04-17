from collections import OrderedDict


# decorator to log return
def log(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(f"func: {func.__name__} {args[1:]} has returned: {res}\n")
        return res

    return wrapper


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    @log
    def get(self, key: int) -> int:
        print(f"get:{key}")
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return -1

    @log
    def put(self, key, value):
        print(f"put:{key, value}")

        if len(self.cache) == self.capacity:
            if not key in self.cache:
                self.cache.popitem(last=False)

        self.cache[key] = value
        self.cache.move_to_end(key)

        return dict(self.cache)


# Your LRUCache object will be instantiated and called as such:
# [[2],[2,1],[1,1],[2,3],[4,1],[1],[2]]
if __name__ == "__main__":
    lRUCache = LRUCache(2)
    lRUCache.put(2, 1)
    lRUCache.put(1, 1)
    lRUCache.put(2, 3)
    lRUCache.put(4, 1)
    lRUCache.get(1)
    lRUCache.get(2)
