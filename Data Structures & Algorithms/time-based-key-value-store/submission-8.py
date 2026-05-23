class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key][0].append(value)
            self.store[key][1].append(timestamp)
        else:
            self.store[key] = [[],[]]
            self.store[key][0].append(value)
            self.store[key][1].append(timestamp)
        return None


    def get(self, key: str, timestamp: int) -> str:
        
        # we will get a time stamp and a key
        # we need to navigate
        if key not in self.store:
            return ""
        left = 0
        right = len(self.store[key][1])-1

        while left <= right:

            mid = left + (right-left)//2

            if self.store[key][1][mid] == timestamp:
                return self.store[key][0][mid]
            
            elif self.store[key][1][mid] > timestamp:
                right = mid - 1
            
            elif self.store[key][1][mid] < timestamp:
                left = mid + 1
        if self.store[key][1][right] < timestamp:
            return self.store[key][0][right]
        else:
            return ""
