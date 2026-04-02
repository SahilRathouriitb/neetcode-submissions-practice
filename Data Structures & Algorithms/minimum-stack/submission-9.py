class MinStack:

    def __init__(self):
        self.top_item = None
        self.l = []
        self.min = []

    def push(self, val: int) -> None:
        self.l.append(val)
        if len(self.l) == 1:
            self.min.append(val)
        
        elif val <=self.min[-1]:
            self.min.append(val)
        
        
        

    def pop(self) -> None:
        a = self.l.pop()
        if a == self.min[-1]:
            self.min.pop()


    def top(self) -> int:
        return self.l[-1]
        

    def getMin(self) -> int:

       
        
            return self.min[-1]

        
