# generated with class generator.python.function$Import
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out.math._rsi import RSI
@registry.expose(["RSI", "Value"])
class Value_mathRSI(IFunctionfloat):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.math._rsi import RSI_IObservableFloatFloatFloat as _math_RSI_IObservableFloatFloatFloat
        from marketsim import deref_opt
        self.x = x if x is not None else deref_opt(_math_RSI_IObservableFloatFloatFloat())
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : RSI
    }
    
    
    def __repr__(self):
        return "Value(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        self.x.bind_ex(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.impl.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        
        self.x.reset_ex(generation)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.impl.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def typecheck(self):
        from marketsim import rtti
        from marketsim.gen._out.math._rsi import RSI
        rtti.typecheck(RSI, self.x)
    
    def registerIn(self, registry):
        if self.__dict__.get('_id', False): return
        self.__dict__['_id'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        registry.insert(self)
        self.x.registerIn(registry)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.registerIn(registry)
        self.impl.registerIn(registry)
        self.__dict__['_processing_ex'] = False
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    _internals = ['impl']
    def __call__(self, *args, **kwargs):
        return self.impl()
    
    def reset(self):
        from marketsim import context
        self.impl = self.getImpl()
        ctx_ex = getattr(self, '_ctx_ex', None)
        if ctx_ex: self.impl.bind_ex(ctx_ex)
        
    
    def getImpl(self):
        from marketsim.gen._out.ops._div import Div_FloatFloat as _ops_Div_FloatFloat
        from marketsim.gen._out.ops._add import Add_FloatFloat as _ops_Add_FloatFloat
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.math._raw import Raw_mathRSI as _math_Raw_mathRSI
        from marketsim.gen._out.ops._sub import Sub_FloatFloat as _ops_Sub_FloatFloat
        from marketsim import deref_opt
        return deref_opt(_ops_Sub_FloatFloat(deref_opt(_constant_Float(100.0)),deref_opt(_ops_Div_FloatFloat(deref_opt(_constant_Float(100.0)),deref_opt(_ops_Add_FloatFloat(deref_opt(_constant_Float(1.0)),deref_opt(_math_Raw_mathRSI(self.x))))))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
# generated with class generator.python.function$Import
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out.math._macd import macd
@registry.expose(["MACD", "Value"])
class Value_mathmacd(IFunctionfloat):
    """ **Moving average convergence/divergence**
    
    
    Parameters are:
    
    **x**
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.math._macd import macd_IObservableFloatFloatFloat as _math_macd_IObservableFloatFloatFloat
        from marketsim import deref_opt
        self.x = x if x is not None else deref_opt(_math_macd_IObservableFloatFloatFloat())
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : macd
    }
    
    
    def __repr__(self):
        return "Value(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        self.x.bind_ex(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.impl.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        
        self.x.reset_ex(generation)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.impl.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def typecheck(self):
        from marketsim import rtti
        from marketsim.gen._out.math._macd import macd
        rtti.typecheck(macd, self.x)
    
    def registerIn(self, registry):
        if self.__dict__.get('_id', False): return
        self.__dict__['_id'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        registry.insert(self)
        self.x.registerIn(registry)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.registerIn(registry)
        self.impl.registerIn(registry)
        self.__dict__['_processing_ex'] = False
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    _internals = ['impl']
    def __call__(self, *args, **kwargs):
        return self.impl()
    
    def reset(self):
        from marketsim import context
        self.impl = self.getImpl()
        ctx_ex = getattr(self, '_ctx_ex', None)
        if ctx_ex: self.impl.bind_ex(ctx_ex)
        
    
    def getImpl(self):
        from marketsim.gen._out.math._avg import Avg_mathEW as _math_Avg_mathEW
        from marketsim.gen._out.math._source import Source_mathmacd as _math_Source_mathmacd
        from marketsim.gen._out.math._slow import Slow_mathmacd as _math_Slow_mathmacd
        from marketsim.gen._out.math._fast import Fast_mathmacd as _math_Fast_mathmacd
        from marketsim.gen._out.ops._sub import Sub_FloatFloat as _ops_Sub_FloatFloat
        from marketsim.gen._out.math._ew import EW_IObservableFloatFloat as _math_EW_IObservableFloatFloat
        from marketsim import deref_opt
        return deref_opt(_ops_Sub_FloatFloat(deref_opt(_math_Avg_mathEW(deref_opt(_math_EW_IObservableFloatFloat(deref_opt(_math_Source_mathmacd(self.x)),(2.0/((deref_opt(_math_Fast_mathmacd(self.x))+1))))))),deref_opt(_math_Avg_mathEW(deref_opt(_math_EW_IObservableFloatFloat(deref_opt(_math_Source_mathmacd(self.x)),(2.0/((deref_opt(_math_Slow_mathmacd(self.x))+1)))))))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
def Value(x = None): 
    from marketsim.gen._out.math._rsi import RSI
    from marketsim.gen._out.math._macd import macd
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, RSI):
        return Value_mathRSI(x)
    if x is None or rtti.can_be_casted(x, macd):
        return Value_mathmacd(x)
    raise Exception('Cannot find suitable overload for Value('+str(x) +':'+ str(type(x))+')')
