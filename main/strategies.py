import backtrader as bt

class TestStrategy(bt.Strategy):

    def log(self, txt, dt=None):
        ''' Logging function for this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        # Keep a reference to the "close" line in the data[0] dataseries
        self.dataclose = self.datas[0].close
        self.order =  None

    def notify_order(self, order) :
        if order.status in [order.Submitted, order.Accepted] :
            print(order.status)
            print(order.Accepted)
            return

        if order.status in [order.Completed] :
            if order.isbuy() :
                self.log(f'BUY EXECUTED{order.executed.price}')
            elif order.issell():
                self.log(f'SELL EXECUTED{order.executed.price}')
            self.bar_executed =  len(self)
        else :
            print(order.status)
        self.order = None
   
    def next(self):
        # Simply log the closing price of the series from the reference
        if self.order : 
            return
        if not self.position :

            self.log('Close, %.2f' % self.dataclose[0])
            if self.dataclose[0] < self.dataclose[-1] : 
                if self.dataclose[-1] < self.dataclose[-2] :

                    self.log('BUY CREATE, %2f' % self.dataclose[0])
                    self.order = self.buy()
        else:
            if len(self) >= (self.bar_executed + 5) :
                self.log(f'SELL CREATED{self.dataclose[0]}')
                self.order = self.sell()

