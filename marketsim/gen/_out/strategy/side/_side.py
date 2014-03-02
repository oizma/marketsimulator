from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out.strategy.side._noise import Noise
from marketsim import context
@registry.expose(["Side function", "Side"])
class Side_strategysideNoise(IFunctionSide):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.strategy.side._noise import Noise_Float as _strategy_side_Noise_Float
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_strategy_side_Noise_Float())
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : Noise
    }
    def __repr__(self):
        return "Side(%(x)s)" % self.__dict__
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    _internals = ['impl']
    def __call__(self, *args, **kwargs):
        return self.impl()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def getImpl(self):
        from marketsim.gen._out.ops._greater import Greater_FloatFloat as _ops_Greater_FloatFloat
        from marketsim import deref_opt
        from marketsim.gen._out.side._buy import Buy_ as _side_Buy_
        from marketsim.gen._out.ops._condition import Condition_BooleanSideSide as _ops_Condition_BooleanSideSide
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.strategy.side._side_distribution import Side_distribution_strategysideNoise as _strategy_side_Side_distribution_strategysideNoise
        return deref_opt(_ops_Condition_BooleanSideSide(deref_opt(_ops_Greater_FloatFloat(deref_opt(_strategy_side_Side_distribution_strategysideNoise(self.x)),deref_opt(_constant_Float(0.5)))),deref_opt(_side_Sell_()),deref_opt(_side_Buy_())))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
from marketsim.gen._out._side import Side
from marketsim.gen._out.strategy.side._meanreversion import MeanReversion
from marketsim import registry
from marketsim import context
from marketsim.gen._out._observable._observableside import ObservableSide
@registry.expose(["Side function", "Side"])
class Side_strategysideMeanReversion(ObservableSide):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim import deref_opt
        from marketsim.gen._out._observable._observableside import ObservableSide
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out.strategy.side._meanreversion import MeanReversion_FloatIOrderBook as _strategy_side_MeanReversion_FloatIOrderBook
        from marketsim.gen._out._side import Side
        from marketsim import event
        ObservableSide.__init__(self)
        self.x = x if x is not None else deref_opt(_strategy_side_MeanReversion_FloatIOrderBook())
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : MeanReversion
    }
    def __repr__(self):
        return "Side(%(x)s)" % self.__dict__
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    _internals = ['impl']
    def __call__(self, *args, **kwargs):
        return self.impl()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def getImpl(self):
        from marketsim.gen._out.strategy.side._book import Book_strategysideMeanReversion as _strategy_side_Book_strategysideMeanReversion
        from marketsim.gen._out.math._avg import Avg_mathEW as _math_Avg_mathEW
        from marketsim import deref_opt
        from marketsim.gen._out.orderbook._midprice import MidPrice_IOrderBook as _orderbook_MidPrice_IOrderBook
        from marketsim.gen._out.math._ew import EW_IObservableFloatFloat as _math_EW_IObservableFloatFloat
        from marketsim.gen._out.strategy.side._fv_side import FV_Side_strategysideFundamentalValue as _strategy_side_FV_Side_strategysideFundamentalValue
        from marketsim.gen._out.strategy.side._alpha import Alpha_strategysideMeanReversion as _strategy_side_Alpha_strategysideMeanReversion
        from marketsim.gen._out.strategy.side._fundamentalvalue import FundamentalValue_FloatIOrderBook as _strategy_side_FundamentalValue_FloatIOrderBook
        return deref_opt(_strategy_side_FV_Side_strategysideFundamentalValue(deref_opt(_strategy_side_FundamentalValue_FloatIOrderBook(deref_opt(_math_Avg_mathEW(deref_opt(_math_EW_IObservableFloatFloat(deref_opt(_orderbook_MidPrice_IOrderBook(deref_opt(_strategy_side_Book_strategysideMeanReversion(self.x)))),deref_opt(_strategy_side_Alpha_strategysideMeanReversion(self.x)))))),deref_opt(_strategy_side_Book_strategysideMeanReversion(self.x))))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out.strategy.side._rsibis import RSIbis
from marketsim import context
@registry.expose(["Side function", "Side"])
class Side_strategysideRSIbis(IFunctionSide):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.strategy.side._rsibis import RSIbis_FloatFloatFloat as _strategy_side_RSIbis_FloatFloatFloat
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_strategy_side_RSIbis_FloatFloatFloat())
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : RSIbis
    }
    def __repr__(self):
        return "Side(%(x)s)" % self.__dict__
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    _internals = ['impl']
    def __call__(self, *args, **kwargs):
        return self.impl()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def getImpl(self):
        from marketsim.gen._out.strategy.side._alpha import Alpha_strategysideRSIbis as _strategy_side_Alpha_strategysideRSIbis
        from marketsim.gen._out.strategy.side._timeframe import Timeframe_strategysideRSIbis as _strategy_side_Timeframe_strategysideRSIbis
        from marketsim.gen._out.math._rsi import RSI_IOrderBookFloatFloat as _math_RSI_IOrderBookFloatFloat
        from marketsim import deref_opt
        from marketsim.gen._out.strategy.side._threshold import Threshold_strategysideRSIbis as _strategy_side_Threshold_strategysideRSIbis
        from marketsim.gen._out.orderbook._oftrader import OfTrader_IAccount as _orderbook_OfTrader_IAccount
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.strategy.side._signal import Signal_FloatFloat as _strategy_side_Signal_FloatFloat
        from marketsim.gen._out.ops._sub import Sub_FloatFloat as _ops_Sub_FloatFloat
        from marketsim.gen._out.strategy.side._s_side import S_Side_strategysideSignal as _strategy_side_S_Side_strategysideSignal
        return deref_opt(_strategy_side_S_Side_strategysideSignal(deref_opt(_strategy_side_Signal_FloatFloat(deref_opt(_ops_Sub_FloatFloat(deref_opt(_constant_Float(50.0)),deref_opt(_math_RSI_IOrderBookFloatFloat(deref_opt(_orderbook_OfTrader_IAccount()),deref_opt(_strategy_side_Timeframe_strategysideRSIbis(self.x)),deref_opt(_strategy_side_Alpha_strategysideRSIbis(self.x)))))),(50.0-deref_opt(_strategy_side_Threshold_strategysideRSIbis(self.x)))))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
from marketsim.gen._out._side import Side
from marketsim.gen._out.strategy.side._fundamentalvalue import FundamentalValue
from marketsim import registry
from marketsim import context
from marketsim.gen._out._observable._observableside import ObservableSide
@registry.expose(["Side function", "Side"])
class Side_strategysideFundamentalValue(ObservableSide):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim import deref_opt
        from marketsim.gen._out._observable._observableside import ObservableSide
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out._side import Side
        from marketsim import event
        from marketsim.gen._out.strategy.side._fundamentalvalue import FundamentalValue_FloatIOrderBook as _strategy_side_FundamentalValue_FloatIOrderBook
        ObservableSide.__init__(self)
        self.x = x if x is not None else deref_opt(_strategy_side_FundamentalValue_FloatIOrderBook())
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : FundamentalValue
    }
    def __repr__(self):
        return "Side(%(x)s)" % self.__dict__
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    _internals = ['impl']
    def __call__(self, *args, **kwargs):
        return self.impl()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def getImpl(self):
        from marketsim.gen._out.strategy.side._fv_side import FV_Side_strategysideFundamentalValue as _strategy_side_FV_Side_strategysideFundamentalValue
        from marketsim import deref_opt
        return deref_opt(_strategy_side_FV_Side_strategysideFundamentalValue(self.x))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out.strategy.side._trendfollower import TrendFollower
from marketsim import context
@registry.expose(["Side function", "Side"])
class Side_strategysideTrendFollower(IFunctionSide):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.strategy.side._trendfollower import TrendFollower_FloatFloatIOrderBook as _strategy_side_TrendFollower_FloatFloatIOrderBook
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_strategy_side_TrendFollower_FloatFloatIOrderBook())
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : TrendFollower
    }
    def __repr__(self):
        return "Side(%(x)s)" % self.__dict__
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    _internals = ['impl']
    def __call__(self, *args, **kwargs):
        return self.impl()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def getImpl(self):
        from marketsim.gen._out.math._avg import Avg_mathEW as _math_Avg_mathEW
        from marketsim import deref_opt
        from marketsim.gen._out.strategy.side._book import Book_strategysideTrendFollower as _strategy_side_Book_strategysideTrendFollower
        from marketsim.gen._out.orderbook._midprice import MidPrice_IOrderBook as _orderbook_MidPrice_IOrderBook
        from marketsim.gen._out.strategy.side._alpha import Alpha_strategysideTrendFollower as _strategy_side_Alpha_strategysideTrendFollower
        from marketsim.gen._out.math._ew import EW_IObservableFloatFloat as _math_EW_IObservableFloatFloat
        from marketsim.gen._out.strategy.side._threshold import Threshold_strategysideTrendFollower as _strategy_side_Threshold_strategysideTrendFollower
        from marketsim.gen._out.math._derivative import Derivative_IDifferentiable as _math_Derivative_IDifferentiable
        from marketsim.gen._out.strategy.side._signal import Signal_FloatFloat as _strategy_side_Signal_FloatFloat
        from marketsim.gen._out.strategy.side._s_side import S_Side_strategysideSignal as _strategy_side_S_Side_strategysideSignal
        return deref_opt(_strategy_side_S_Side_strategysideSignal(deref_opt(_strategy_side_Signal_FloatFloat(deref_opt(_math_Derivative_IDifferentiable(deref_opt(_math_Avg_mathEW(deref_opt(_math_EW_IObservableFloatFloat(deref_opt(_orderbook_MidPrice_IOrderBook(deref_opt(_strategy_side_Book_strategysideTrendFollower(self.x)))),deref_opt(_strategy_side_Alpha_strategysideTrendFollower(self.x)))))))),deref_opt(_strategy_side_Threshold_strategysideTrendFollower(self.x))))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out.strategy.side._crossingaverages import CrossingAverages
from marketsim import context
@registry.expose(["Side function", "Side"])
class Side_strategysideCrossingAverages(IFunctionSide):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.strategy.side._crossingaverages import CrossingAverages_FloatFloatFloatIOrderBook as _strategy_side_CrossingAverages_FloatFloatFloatIOrderBook
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_strategy_side_CrossingAverages_FloatFloatFloatIOrderBook())
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : CrossingAverages
    }
    def __repr__(self):
        return "Side(%(x)s)" % self.__dict__
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    _internals = ['impl']
    def __call__(self, *args, **kwargs):
        return self.impl()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def getImpl(self):
        from marketsim.gen._out.math._avg import Avg_mathEW as _math_Avg_mathEW
        from marketsim import deref_opt
        from marketsim.gen._out.orderbook._midprice import MidPrice_IOrderBook as _orderbook_MidPrice_IOrderBook
        from marketsim.gen._out.math._ew import EW_IObservableFloatFloat as _math_EW_IObservableFloatFloat
        from marketsim.gen._out.strategy.side._book import Book_strategysideCrossingAverages as _strategy_side_Book_strategysideCrossingAverages
        from marketsim.gen._out.strategy.side._threshold import Threshold_strategysideCrossingAverages as _strategy_side_Threshold_strategysideCrossingAverages
        from marketsim.gen._out.strategy.side._alpha_1 import Alpha_1_strategysideCrossingAverages as _strategy_side_Alpha_1_strategysideCrossingAverages
        from marketsim.gen._out.strategy.side._signal import Signal_FloatFloat as _strategy_side_Signal_FloatFloat
        from marketsim.gen._out.ops._sub import Sub_FloatFloat as _ops_Sub_FloatFloat
        from marketsim.gen._out.strategy.side._alpha_2 import Alpha_2_strategysideCrossingAverages as _strategy_side_Alpha_2_strategysideCrossingAverages
        from marketsim.gen._out.strategy.side._s_side import S_Side_strategysideSignal as _strategy_side_S_Side_strategysideSignal
        return deref_opt(_strategy_side_S_Side_strategysideSignal(deref_opt(_strategy_side_Signal_FloatFloat(deref_opt(_ops_Sub_FloatFloat(deref_opt(_math_Avg_mathEW(deref_opt(_math_EW_IObservableFloatFloat(deref_opt(_orderbook_MidPrice_IOrderBook(deref_opt(_strategy_side_Book_strategysideCrossingAverages(self.x)))),deref_opt(_strategy_side_Alpha_1_strategysideCrossingAverages(self.x)))))),deref_opt(_math_Avg_mathEW(deref_opt(_math_EW_IObservableFloatFloat(deref_opt(_orderbook_MidPrice_IOrderBook(deref_opt(_strategy_side_Book_strategysideCrossingAverages(self.x)))),deref_opt(_strategy_side_Alpha_2_strategysideCrossingAverages(self.x)))))))),deref_opt(_strategy_side_Threshold_strategysideCrossingAverages(self.x))))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out.strategy.side._signal import Signal
from marketsim import context
@registry.expose(["Side function", "Side"])
class Side_strategysideSignal(IFunctionSide):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.strategy.side._signal import Signal_FloatFloat as _strategy_side_Signal_FloatFloat
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_strategy_side_Signal_FloatFloat())
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : Signal
    }
    def __repr__(self):
        return "Side(%(x)s)" % self.__dict__
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    _internals = ['impl']
    def __call__(self, *args, **kwargs):
        return self.impl()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def getImpl(self):
        from marketsim.gen._out.strategy.side._s_side import S_Side_strategysideSignal as _strategy_side_S_Side_strategysideSignal
        from marketsim import deref_opt
        return deref_opt(_strategy_side_S_Side_strategysideSignal(self.x))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
from marketsim.gen._out.strategy.side._pairtrading import PairTrading
from marketsim.gen._out._side import Side
from marketsim import registry
from marketsim import context
from marketsim.gen._out._observable._observableside import ObservableSide
@registry.expose(["Side function", "Side"])
class Side_strategysidePairTrading(ObservableSide):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim import deref_opt
        from marketsim.gen._out._observable._observableside import ObservableSide
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out._side import Side
        from marketsim.gen._out.strategy.side._pairtrading import PairTrading_IOrderBookFloatIOrderBook as _strategy_side_PairTrading_IOrderBookFloatIOrderBook
        from marketsim import event
        ObservableSide.__init__(self)
        self.x = x if x is not None else deref_opt(_strategy_side_PairTrading_IOrderBookFloatIOrderBook())
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : PairTrading
    }
    def __repr__(self):
        return "Side(%(x)s)" % self.__dict__
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    _internals = ['impl']
    def __call__(self, *args, **kwargs):
        return self.impl()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def getImpl(self):
        from marketsim.gen._out.strategy.side._factor import Factor_strategysidePairTrading as _strategy_side_Factor_strategysidePairTrading
        from marketsim import deref_opt
        from marketsim.gen._out.orderbook._midprice import MidPrice_IOrderBook as _orderbook_MidPrice_IOrderBook
        from marketsim.gen._out.strategy.side._book import Book_strategysidePairTrading as _strategy_side_Book_strategysidePairTrading
        from marketsim.gen._out.strategy.side._booktodependon import BookToDependOn_strategysidePairTrading as _strategy_side_BookToDependOn_strategysidePairTrading
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.strategy.side._fv_side import FV_Side_strategysideFundamentalValue as _strategy_side_FV_Side_strategysideFundamentalValue
        from marketsim.gen._out.ops._mul import Mul_IObservableFloatFloat as _ops_Mul_IObservableFloatFloat
        from marketsim.gen._out.strategy.side._fundamentalvalue import FundamentalValue_FloatIOrderBook as _strategy_side_FundamentalValue_FloatIOrderBook
        return deref_opt(_strategy_side_FV_Side_strategysideFundamentalValue(deref_opt(_strategy_side_FundamentalValue_FloatIOrderBook(deref_opt(_ops_Mul_IObservableFloatFloat(deref_opt(_orderbook_MidPrice_IOrderBook(deref_opt(_strategy_side_BookToDependOn_strategysidePairTrading(self.x)))),deref_opt(_constant_Float(deref_opt(_strategy_side_Factor_strategysidePairTrading(self.x)))))),deref_opt(_strategy_side_Book_strategysidePairTrading(self.x))))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
def Side(x = None): 
    from marketsim import rtti
    from marketsim.gen._out.strategy.side._noise import Noise
    from marketsim.gen._out.strategy.side._meanreversion import MeanReversion
    from marketsim.gen._out.strategy.side._signal import Signal
    from marketsim.gen._out.strategy.side._crossingaverages import CrossingAverages
    from marketsim.gen._out.strategy.side._rsibis import RSIbis
    from marketsim.gen._out.strategy.side._fundamentalvalue import FundamentalValue
    from marketsim.gen._out.strategy.side._trendfollower import TrendFollower
    from marketsim.gen._out.strategy.side._pairtrading import PairTrading
    if x is None or rtti.can_be_casted(x, Noise):
        return Side_strategysideNoise(x)
    if x is None or rtti.can_be_casted(x, MeanReversion):
        return Side_strategysideMeanReversion(x)
    if x is None or rtti.can_be_casted(x, RSIbis):
        return Side_strategysideRSIbis(x)
    if x is None or rtti.can_be_casted(x, FundamentalValue):
        return Side_strategysideFundamentalValue(x)
    if x is None or rtti.can_be_casted(x, TrendFollower):
        return Side_strategysideTrendFollower(x)
    if x is None or rtti.can_be_casted(x, CrossingAverages):
        return Side_strategysideCrossingAverages(x)
    if x is None or rtti.can_be_casted(x, Signal):
        return Side_strategysideSignal(x)
    if x is None or rtti.can_be_casted(x, PairTrading):
        return Side_strategysidePairTrading(x)
    raise Exception('Cannot find suitable overload for Side('+str(x) +':'+ str(type(x))+')')
