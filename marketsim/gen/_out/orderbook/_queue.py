# generated with class generator.python.intrinsic_function$Import
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._intrinsic.orderbook.proxy import Queue_Impl
from marketsim.gen._out._iorderqueue import IOrderQueue
@registry.expose(["Asset", "Queue"])
class Queue_IOrderBookSide(IOrderQueue,Queue_Impl):
    """ **Returns order queue of order *book* for trade *side***
    
    
    Parameters are:
    
    **book**
    
    **side**
    """ 
    def __init__(self, book = None, side = None):
        from marketsim.gen._out.orderbook._oftrader import OfTrader_IAccount as _orderbook_OfTrader_IAccount
        from marketsim import deref_opt
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        self.book = book if book is not None else deref_opt(_orderbook_OfTrader_IAccount())
        self.side = side if side is not None else deref_opt(_side_Sell_())
        Queue_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'book' : IOrderBook,
        'side' : IFunctionSide
    }
    
    
    
    
    def __repr__(self):
        return "Queue(%(book)s, %(side)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.bind_ex(self.__dict__['_ctx_ex'])
                else:
                    v.bind_ex(self.__dict__['_ctx_ex'])
        self.book.bind_ex(self._ctx_ex)
        self.side.bind_ex(self._ctx_ex)
        self.bind_impl(self.__dict__['_ctx_ex'])
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.reset_ex(generation)
                else:
                    v.reset_ex(generation)
        self.book.reset_ex(generation)
        self.side.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def typecheck(self):
        from marketsim import rtti
        from marketsim.gen._out._iorderbook import IOrderBook
        from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
        rtti.typecheck(IOrderBook, self.book)
        rtti.typecheck(IFunctionSide, self.side)
    
    def registerIn(self, registry):
        if self.__dict__.get('_id', False): return
        self.__dict__['_id'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        registry.insert(self)
        self.book.registerIn(registry)
        self.side.registerIn(registry)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.registerIn(registry)
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.registerIn(registry)
                else:
                    v.registerIn(registry)
        self.__dict__['_processing_ex'] = False
    
    def bind_impl(self, ctx):
        Queue_Impl.bind_impl(self, ctx)
    
    def reset(self):
        Queue_Impl.reset(self)
    
def Queue(book = None,side = None): 
    from marketsim.gen._out._iorderbook import IOrderBook
    from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
    from marketsim import rtti
    if book is None or rtti.can_be_casted(book, IOrderBook):
        if side is None or rtti.can_be_casted(side, IFunctionSide):
            return Queue_IOrderBookSide(book,side)
    raise Exception('Cannot find suitable overload for Queue('+str(book) +':'+ str(type(book))+','+str(side) +':'+ str(type(side))+')')
