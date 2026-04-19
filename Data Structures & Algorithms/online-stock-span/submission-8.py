class StockSpanner:

    def __init__(self):
        self.l = []
        

    def next(self, price: int) -> int:
        span = 1

        while len(self.l)>0 and self.l[-1][0] <= price:

            span = span + self.l[-1][1]
            self.l.pop()

        
        self.l.append([price,span])

        return self.l[-1][1]
        


