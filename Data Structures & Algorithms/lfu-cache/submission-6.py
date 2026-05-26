class LFUCache:

    def __init__(self, capacity: int):
        self.store = {}
        self.cache = [] # This can have a max size of 2
        self.cnt = {}
        self.capacity = capacity
        self.filled = 0
        

    def get(self, key: int) -> int:
        if key in self.store:
            self.cnt[key] += 1
            # Updating cache list with the key
            if len(self.cache) >= self.cnt[key]:
                self.cache[self.cnt[key]-1].append(key)
            else:
                self.cache.append([])
                self.cache[-1].append(key)
            if self.cnt[key] > 1:
                self.cache[self.cnt[key]-2].remove(key)

            return self.store[key]

        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        # Let's firstly add it to the store
        if key in self.store:
            self.store[key] = value
            self.cnt[key] += 1
            # Updating cache list with the key
            if len(self.cache) >= self.cnt[key]:
                self.cache[self.cnt[key]-1].append(key)
            else:
                self.cache.append([])
                self.cache[-1].append(key)
            if self.cnt[key] > 1:
                self.cache[self.cnt[key]-2].remove(key)

        elif self.filled < self.capacity:
            self.store[key] = value
            self.cnt[key] = 1
            self.filled += 1
            # Updating cache list with the key and removal from the previous index
            if len(self.cache) >0:
                self.cache[0].append(key)
            else:
                self.cache.append([])
                self.cache[0].append(key)

        elif self.filled == self.capacity:
            # If it is filled, we need to remove one first
            k = None
            for i in range(len(self.cache)):
                if len(self.cache[i])>0:
                    k = self.cache[i].pop(0)
                    break
            self.store.pop(k)
            self.cnt.pop(k)
            self.filled -= 1

            # Now we have the space
            self.store[key] = value
            self.cnt[key] = 1
            self.filled += 1
            if len(self.cache) >0:
                self.cache[0].append(key)
            else:
                self.cache.append([])
                self.cache[0].append(key)
