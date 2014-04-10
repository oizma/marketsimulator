# generated with class generator.python.accessor$Import
from marketsim import registry
from marketsim.gen._out.strategy.price._liquidityprovider import LiquidityProvider
@registry.expose(["-", "Book"])
class Book_strategypriceLiquidityProvider(object):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.strategy.price._liquidityprovider import LiquidityProvider_FloatFloatIOrderBook as _strategy_price_LiquidityProvider_FloatFloatIOrderBook
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_strategy_price_LiquidityProvider_FloatFloatIOrderBook())
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : LiquidityProvider
    }
    
    
    def __repr__(self):
        return "Book(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_bound_ex'): return
        self._bound_ex = True
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        self._processing_ex = True
        self._ctx_ex = ctx
        self.x.bind_ex(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self._ctx_ex)
        delattr(self, '_processing_ex')
    
    @property
    def dereference(self):
        return self.x.book
    
def Book(x = None): 
    from marketsim.gen._out.strategy.price._liquidityprovider import LiquidityProvider
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, LiquidityProvider):
        return Book_strategypriceLiquidityProvider(x)
    raise Exception('Cannot find suitable overload for Book('+str(x) +':'+ str(type(x))+')')