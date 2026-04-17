class StockSpanner:

    def __init__(self):
        self.l = []
        

    def next(self, price: int) -> int:
        counter = 0
        self.l.append(price)
        for i in self.l[::-1]:
            if i <= price:
                counter = counter + 1
            else:
                break
        return counter


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)