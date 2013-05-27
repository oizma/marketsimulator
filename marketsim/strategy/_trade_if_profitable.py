from marketsim import (trader, order, orderbook, scheduler, observable, order, 
                       registry, types, meta, bind, mathutils, event)

from marketsim.types import *

from _basic import Strategy
from _wrap import wrapper2
from _fv import FundamentalValue

class _tradeIfProfitable_Impl(Strategy):

    def _wakeUp_impl(self, _):
        if not self.suspended:
            self._strategy.suspend(self._efficiency.value < 0)

    def __init__(self):
        Strategy.__init__(self)
        self._estimator_strategy = self.estimator(self.strategy) # TODO: dependency tracking
        self._estimator = trader.SASM(orderbook.OfTrader(trader.SASM_ParentProxy()),
                                      self._estimator_strategy)

        self._strategy = self.strategy
        self._efficiency = self.efficiency(self._estimator) # TODO: dependency tracking
        
        event.subscribe(self._efficiency.on_changed, bind.Method(self, '_wakeUp_impl'))
        
    _internals = ['_estimator', '_efficiency']
        
    def updateContext(self, context):
        context.parentTrader = context.trader
                
    def dispose(self):
        self._strategy.dispose()
        self._estimator_strategy.dispose()
        
    def suspend(self, s=True):
        Strategy.suspend(self, s)
        self._strategy.suspend(s)
        self._estimator_strategy.suspend(s)

@registry.expose(alias=["trader's efficiency trend"])
@sig(args=(ISingleAssetTrader,), rv=ISingleAssetTrader)
def efficiencyTrend(trader):
    """ Returns derivative of a *trader*'s "cleared" balance
    """
    return observable.trend(observable.Efficiency(trader))

@registry.expose(alias=['Virtual market orders with unit volume'])
@sig(args=(IStrategy,), rv=IStrategy)
def virtualWithUnitVolume(strategy):
    """ Creates for a *strategy* a clone with same parameters but sending virtual market orders of unit volume
    """
    return strategy.With(volumeDistr=mathutils.constant(1), orderFactory=order.VirtualMarketFactory)    

exec wrapper2("tradeIfProfitable", 
             "",
             [('strategy',   'FundamentalValue()',    'IStrategy'), 
              ('efficiency', 'efficiencyTrend',       'ISingleAssetTrader -> ISingleAssetTrader'),
              ('estimator',  'virtualWithUnitVolume', 'IStrategy -> IStrategy')], register=False)

        
@registry.expose(['Adaptive', 'TradeIfProfitable'])
class TradeIfProfitable(tradeIfProfitable):
    """ Strategy that estimates efficiency of original *strategy* 
    (normally as derivative of "cleared" balance for its clone sending unit volume orders)
    
    Parameters: 
    
        |strategy| 
            original strategy that can be suspended
            
        |efficiency| 
            function estimating is the strategy efficient or not
            
        |estimator| 
            function creating phantom strategy used for efficiency estimation
    """
    
    def __init__(self, strategy = FundamentalValue(), 
                 efficiency=efficiencyTrend, 
                 estimator=virtualWithUnitVolume, 
                 **kwargs):
        tradeIfProfitable.__init__(self, strategy.With(**kwargs), efficiency, estimator)
        self._constructAs = 'marketsim.strategy.TradeIfProfitable'
    
    def With(self, 
             strategy = None, 
             efficiency = None,
             estimator = None,
             **kwargs):
        
        if strategy is None: strategy = self.strategy
        
        # TODO: we should also make _properties as union of all members _properties
        # during this union we should also check that there is no conflicts
        # With method should be implemented as walk over _properties
        # but there is no clear answer about what shall we do in case of chooseTheBest 
        # OR: we may consider these classes as decorators to exisiting strategies and believe
        # that parameters are passed to strategies not to 'efficiency' or 'estimator'
        # if someone wants to change 'efficiency' or 'estimator' parameters he should do it explicitly 
        return tradeIfProfitable.With(self, strategy.With(**kwargs), efficiency, estimator)
