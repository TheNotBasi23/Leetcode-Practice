class StockSpanner(object):

    def __init__(self):
        self.mono = []
        self.arr = []

    def next(self, price):
        self.arr.append(price)

        while self.mono and self.arr[self.mono[-1]] <= price:
            self.mono.pop()

        value = len(self.arr) if not self.mono else len(self.arr) - 1 - self.mono[-1]
        self.mono.append(len(self.arr) - 1)

        return value