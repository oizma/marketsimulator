class IAccount(object):
    def Balance(self):
        from marketsim.gen._out.trader._balance import Balance
        return Balance(self)
    
    def RoughPnL(self):
        from marketsim.gen._out.trader._roughpnl import RoughPnL
        return RoughPnL(self)
    
    def Position(self):
        from marketsim.gen._out.trader._position import Position
        return Position(self)
    
    def Efficiency(self):
        from marketsim.gen._out.trader._efficiency import Efficiency
        return Efficiency(self)
    
    def OfTrader(self):
        from marketsim.gen._out.orderbook._oftrader import OfTrader
        return OfTrader(self)
    
    def EfficiencyTrend(self, alpha = None):
        from marketsim.gen._out.trader._efficiencytrend import EfficiencyTrend
        return EfficiencyTrend(self,alpha)
    
    def PendingVolume(self):
        from marketsim.gen._out.trader._pendingvolume import PendingVolume
        return PendingVolume(self)
    
    pass
