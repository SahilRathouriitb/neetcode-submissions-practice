class StockSpanner:

    def __init__(self):
        self.l = []
        

    def next(self, price: int) -> int:
        counter = 1
        if len(self.l) == 0:
            self.l.append([price,counter])
        else:
            for i in self.l[::-1]:

                if price == i[0]:
                    i[1] += 1
                    #print(self.l)
                    break
                
                elif price > i[0]:
                    counter = counter + i[1]
                    #print('ok')
                    self.l.pop()
                    if len(self.l) == 0:
                        self.l.append([price,counter])
                    #print(self.l)
    
                elif price < i[0]:
                    self.l.append([price,counter])
                    #print(self.l)
                    break
                    
        
        return self.l[-1][1]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)