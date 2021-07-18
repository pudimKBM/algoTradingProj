import backtrader as bt
from datetime import datetime
import backtrader.feeds as btfeeds
from strategies import TestStrategy


import pandas
import backtrader.feeds as btfeeds



cerebro = bt.Cerebro()
cerebro.broker.setcash(500)

dataname="C:/Users/anton/Documents/GitHub/algoTradingProj/data/US30.csv"


data = btfeeds.GenericCSVData(
        dataname=dataname,

        fromdate=datetime(2018, 1, 1),
        todate=datetime(2019, 1, 1),
        timeframe=btfeeds.TimeFrame.Minutes,
        nullvalue=0.0,

        dtformat=("%d.%m.%Y %H:%M:%S.%f"),
        datetime=0,
        high=2,
        low=3,
        open=1,
        close=4,
        volume=5,
        openinterest=-1,
        compression=60

        )

cerebro.adddata(data)


cerebro.addstrategy(TestStrategy)

cerebro.addsizer(bt.sizers.FixedSize, stake = 0.1)
print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

cerebro.run()

print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

cerebro.plot()
