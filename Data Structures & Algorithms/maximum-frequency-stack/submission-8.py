class FreqStack:

    def __init__(self):
        self.stack = []
        self.dic = {}         

    def push(self, val: int) -> None:

        self.stack.append(val)
        if val not in self.dic:
            self.dic[val] = 1
        else:
            self.dic[val] = self.dic[val] + 1

    def most_frequent(self):
        b = self.dic.values()
        m = max(b)
        return [i for i in self.dic if (self.dic[i] == m)]
        
    def pop(self) -> int:
        mn = self.most_frequent()
        k = -1
        for i in range(len(self.stack)-1, -1,-1):
            #print(i)
            if self.stack[i] in mn:
                k = self.stack[i]
                self.dic[self.stack[i]] = self.dic[self.stack[i]] - 1
                self.stack[i] = None
                break
        #print(self.dic) 
        #print(self.stack)
        return k 
