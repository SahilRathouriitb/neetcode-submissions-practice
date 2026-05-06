class FreqStack:

    def __init__(self):
        self.stack = []
        self.dic = {}
        self.max = 1        

    def push(self, val: int) -> None:

        self.stack.append(val)
        if val not in self.dic:
            self.dic[val] = 1
            if self.max < 1:
                self.max = 1
        else:
            self.dic[val] = self.dic[val] + 1
            self.max = max(self.max, self.dic[val])


    def most_frequent(self):
        return [i for i in self.dic if (self.dic[i] == self.max)]
        
    def pop(self) -> int:
        mn = self.most_frequent()
        if len(mn) == 1:
            self.max -= 1
        k = -1
        for i in range(len(self.stack)-1, -1,-1):
            if self.stack[i] in mn:
                k = self.stack[i]
                self.dic[self.stack[i]] = self.dic[self.stack[i]] - 1
                self.stack[i] = None
                break
        return k 
