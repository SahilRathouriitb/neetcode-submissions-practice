class FreqStack:

    def __init__(self):
        self.stack = [None,[]]
        self.dic = {}
        self.max = 1        

    def push(self, val: int) -> None:

        if (val not in self.dic) or (self.dic[val] == 0):
            self.dic[val] = 1
            self.stack[1].append(val)
            if self.max < 1:
                self.max = 1
        else:
            if len(self.stack)  < (self.max + 2):
                self.stack.append([])
            self.dic[val] += 1
            self.stack[self.dic[val]].append(val)
            self.max = max(self.max, self.dic[val])
        
        
    def pop(self) -> int:
        k = self.stack[self.max].pop()
        self.dic[k] -= 1
        if len(self.stack[self.max]) == 0:
            self.max -= 1
        return k
        
