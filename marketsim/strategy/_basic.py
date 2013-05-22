from marketsim import types

class Strategy(types.IStrategy):
    
    def __init__(self):
        self._suspended = False
        
    @property
    def suspended(self):
        return self._suspended
    
    def suspend(self, s=True):
        self._suspended = s
        
    def bind(self, context):
        self._trader = context.trader
        self._scheduler = context.world    
        
    @property
    def trader(self):
        return self._trader
   