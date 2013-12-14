
package side {
    def Sell() : () => Side
        
    
    def Buy() : () => Side
        
    
    def None() : () => Side
        
}

package mathops {
    /** Arc tangent of x, in radians.
     *
     */
    @python.mathops("Trigonometric", "atan", "atan(%(x)s)")
    def Atan(x = constant(0.0)) : () => Float
        
    
    /** Square root of x
     *
     */
    @python.mathops("Log/Pow", "sqrt", "\\sqrt{%(x)s}")
    def Sqrt(x = constant(1.0)) : () => Float
        
    
    /** Exponent of x
     *
     */
    @python.mathops("Log/Pow", "exp", "e^{%(x)s}")
    def Exp(x = constant(1.0)) : () => Float
        
    
    /** Natural logarithm of x (to base e)
     *
     */
    @python.mathops("Log/Pow", "log", "log(%(x)s)")
    def Log(x = constant(1.0)) : () => Float
        
    
    /** Return *x* raised to the power *y*.
     *
     * Exceptional cases follow Annex F of the C99 standard as far as possible.
     * In particular, ``pow(1.0, x)`` and ``pow(x, 0.0)`` always return 1.0,
     * even when *x* is a zero or a NaN.
     * If both *x* and *y* are finite, *x* is negative, and *y* is not an integer then
     * ``pow(x, y)`` is undefined, and raises ``ValueError``.
     */
    @python.mathops("Log/Pow", "pow", "%(base)s^{%(power)s}")
    def Pow(base = constant(1.0),
            power = constant(1.0)) : () => Float
        
}

package mathutils {
    package rnd {
        /** Gamma distribution
         *
         *  Conditions on the parameters are |alpha| > 0 and |beta| > 0.
         *
         *  The probability distribution function is: ::
         *
         *               x ** (alpha - 1) * math.exp(-x / beta)
         *     pdf(x) =  --------------------------------------
         *                  math.gamma(alpha) * beta ** alpha
         */
        @python.random()
        def gammavariate(Alpha = 1.0,
                         Beta = 1.0) : () => Float
            
        
        /** Normal distribution
         */
        @python.random()
        def normalvariate(/** |mu| is the mean                  */ Mu = 0.0,
                          /** |sigma| is the standard deviation */ Sigma = 1.0) : () => Float
            
        
        /** Pareto distribution
         */
        @python.random()
        def paretovariate(/** |alpha| is the shape parameter*/ Alpha = 1.0) : () => Float
            
        
        /** Triangular distribution
         *
         * Return a random floating point number *N* such that *low* <= *N* <= *high* and
         *       with the specified *mode* between those bounds.
         *       The *low* and *high* bounds default to zero and one.
         *       The *mode* argument defaults to the midpoint between the bounds,
         *       giving a symmetric distribution.
         */
        @python.random()
        def triangular(Low = 0.0,
                       High = 1.0,
                       Mode = 0.5) : () => Float
            
        
        /** Von Mises distribution
         */
        @python.random()
        def vonmisesvariate(/** |mu| is the mean angle, expressed in radians between 0 and 2|pi|*/ Mu = 0.0,
                            /** |kappa| is the concentration parameter, which must be greater than or equal to zero.
                              *      If |kappa| is equal to zero, this distribution reduces
                              *      to a uniform random angle over the range 0 to 2|pi|        */ Kappa = 0.0) : () => Float
            
        
        /** Uniform distribution
         *
         * Return a random floating point number *N* such that
         * *a* <= *N* <= *b* for *a* <= *b* and *b* <= *N* <= *a* for *b* < *a*.
         * The end-point value *b* may or may not be included in the range depending on
         * floating-point rounding in the equation *a* + (*b*-*a*) * *random()*.
         */
        @python.random()
        def uniform(Low = -10.0,
                    High = 10.0) : () => Float
            
        
        /** Weibull distribution
         */
        @python.random()
        def weibullvariate(/** |alpha| is the scale parameter */ Alpha = 1.0,
                           /** |beta| is the shape parameter  */ Beta = 1.0) : () => Float
            
        
        /** Exponential distribution
         *
         *  Returned values range from 0 to positive infinity
         */
        @python.random()
        def expovariate(/** |lambda| is 1.0 divided by the desired mean. It should be greater zero.*/ Lambda = 1.0) : () => Float
            
        
        /** Log normal distribution
         *
         * If you take the natural logarithm of this distribution,
         *  you'll get a normal distribution with mean |mu| and standard deviation |sigma|.
         *  |mu| can have any value, and |sigma| must be greater than zero.
         */
        @python.random()
        def lognormvariate(Mu = 0.0,
                           Sigma = 1.0) : () => Float
            
        
        /** Beta distribution
         *
         * Conditions on the parameters are |alpha| > 0 and |beta| > 0.
         * Returned values range between 0 and 1.
         */
        @python.random()
        def betavariate(Alpha = 1.0,
                        Beta = 1.0) : () => Float
            
    }
}

package observable {
    package sidefunc {
        def PairTrading(dependee = orderbook.OfTrader(),
                        factor = constant(1.0),
                        book = orderbook.OfTrader())
             = FundamentalValue(orderbook.MidPrice(dependee)*factor,book)
        
        def Signal(signal = constant(),
                   threshold = 0.7)
             = if signal>threshold then side.Buy() else if signal<0.0-threshold then side.Sell() else side.None()
        
        def CrossingAverages(alpha_1 = 0.015,
                             alpha_2 = 0.15,
                             threshold = 0.0,
                             book = orderbook.OfTrader())
             = Signal(EW.Avg(orderbook.MidPrice(book),alpha_1)-EW.Avg(orderbook.MidPrice(book),alpha_2),threshold)
        
        def TrendFollower(alpha = 0.015,
                          threshold = 0.0,
                          book = orderbook.OfTrader())
             = Signal(Derivative(EW.Avg(orderbook.MidPrice(book),alpha)),threshold)
        
        def FundamentalValue(fv = constant(200.0),
                             book = orderbook.OfTrader())
             = if orderbook.BidPrice(book)>fv then side.Sell() else if orderbook.AskPrice(book)<fv then side.Buy() else side.None()
        
        def MeanReversion(alpha = 0.015,
                          book = orderbook.OfTrader())
             = FundamentalValue(EW.Avg(orderbook.MidPrice(book),alpha),book)
        
        def Noise(side_distribution = mathutils.rnd.uniform(0.0,1.0))
             = if side_distribution>0.5 then side.Sell() else side.Buy()
    }
    
    package Cumulative {
        @python.intrinsic.function("Statistics", "Avg_{cumul}(%(source)s)", "moments.cma.CMA_Impl")
        def Avg(source = const()) : () => Float
            
        
        @python.intrinsic.function("Statistics", "\\sigma^2_{cumul}(%(source)s)", "moments.cmv.Variance_Impl")
        def Var(source = const()) : () => Float
            
        
        @python.function("Statistics", "\\sqrt{\\sigma^2_{cumul}_{%(source)s}}")
        def StdDev(source = const())
             = mathops.Sqrt(Var(source))
    }
    
    package rsi {
        @python.observable("RSI", "RSI-raw_{%(timeframe)s}^{%(alpha)s}(%(source)s)")
        def Raw(source = orderbook.MidPrice(),
                timeframe = 10.0,
                alpha = 0.015)
             = EW.Avg(UpMovements(source,timeframe),alpha)/EW.Avg(DownMovements(source,timeframe),alpha)
    }
    
    package macd {
        @python.function("MACD", "MACD_{%(fast)s}^{%(slow)s}(%(x)s)")
        def MACD(x = orderbook.MidPrice(),
                 slow = 26.0,
                 fast = 12.0)
             = EW.Avg(x,2.0/(fast+1.0))-EW.Avg(x,2.0/(slow+1.0))
        
        @python.function("MACD", "Signal^{%(timeframe)s}_{%(step)s}(MACD_{%(fast)s}^{%(slow)s}(%(x)s))")
        def Signal(x = orderbook.MidPrice(),
                   slow = 26.0,
                   fast = 12.0,
                   timeframe = 9.0,
                   step = 1.0)
             = EW.Avg(OnEveryDt(step,MACD(x,slow,fast)),2.0/(timeframe+1.0))
        
        @python.function("MACD", "Histogram^{%(timeframe)s}_{%(step)s}(MACD_{%(fast)s}^{%(slow)s}(%(x)s))")
        def Histogram(x = orderbook.MidPrice(),
                      slow = 26.0,
                      fast = 12.0,
                      timeframe = 9.0,
                      step = 1.0)
             = MACD(x,slow,fast)-Signal(x,slow,fast,timeframe,step)
    }
    
    package trader {
        @python.intrinsic.function("Proxies", "N/A", "trader.proxy._Single_Impl")
        def SingleProxy() : ISingleAssetTrader
            
    }
    
    package EW {
        @python.intrinsic.function("Statistics", "Avg_{\\alpha=%(alpha)s}(%(source)s)", "moments.ewma.EWMA_Impl")
        def Avg(source = constant(),
                alpha = 0.015) : IDifferentiable
            
        
        @python.intrinsic.function("Statistics", "\\sigma^2_{\\alpha=%(alpha)s}_{%(source)s}", "moments.ewmv.EWMV_Impl")
        def Var(source = const(),
                alpha = 0.015) : () => Float
            
        
        @python.function("Statistics", "\\sqrt{\\sigma^2_{\\alpha=%(alpha)s}_{%(source)s}}")
        def StdDev(source = const(),
                   alpha = 0.015)
             = mathops.Sqrt(Var(source,alpha))
    }
    
    package orderbook {
        def PriceAtVolume(queue = Asks(),
                          volume = 100.0) : () => Float
            
        
        @python.observable("Orderbook", "Price_{%(alpha)s}^{%(queue)s}")
        def WeightedPrice(queue = Asks(),
                          alpha = 0.015)
             = EW.Avg(LastTradePrice(queue)*LastTradeVolume(queue),alpha)/EW.Avg(LastTradeVolume(queue),alpha)
        
        def TickSize(book = OfTrader()) : () => Float
            
        
        @python.observable("Orderbook", "Ask_{%(book)s}")
        def AskLastPrice(book = OfTrader())
             = LastPrice(Asks(book))
        
        @python.observable("Orderbook", "Ask_{%(alpha)s}^{%(book)s}")
        def AskWeightedPrice(book = OfTrader(),
                             alpha = 0.015)
             = WeightedPrice(Asks(book),alpha)
        
        @python.observable("Orderbook", "MidPrice_{%(book)s}")
        def MidPrice(book = OfTrader())
             = (AskPrice(book)+BidPrice(book))/2.0
        
        @python.intrinsic.function("Queue's", "Asks(%(book)s)", "orderbook.queue._Asks_Impl")
        def Asks(book = OfTrader()) : IOrderQueue
            
        
        @python.observable("Orderbook", "Bid_{%(alpha)s}^{%(book)s}")
        def BidWeightedPrice(book = OfTrader(),
                             alpha = 0.015)
             = WeightedPrice(Bids(book),alpha)
        
        @python.observable("Orderbook", "Ask_{%(book)s}")
        def AskPrice(book = OfTrader())
             = BestPrice(Asks(book))
        
        @python.intrinsic.observable("Orderbook", "LastTradeVolume(%(queue)s)", "orderbook.last_trade._LastTradeVolume_Impl")
        def LastTradeVolume(queue = Asks()) : IObservable
            
        
        @python.observable("Orderbook", "Bid^{%(book)s}")
        def BidPrice(book = OfTrader())
             = BestPrice(Bids(book))
        
        @python.intrinsic.function("Queue's", "Bids(%(book)s)", "orderbook.queue._Bids_Impl")
        def Bids(book = OfTrader()) : IOrderQueue
            
        
        @python.intrinsic.observable("Orderbook", "Price(%(queue)s)", "orderbook.props._BestPrice_Impl")
        def BestPrice(queue = Asks()) : IObservable
            
        
        @python.intrinsic.function("Proxies", "N/A", "orderbook.of_trader._OfTrader_Impl")
        def OfTrader(Trader = trader.SingleProxy()) : IOrderBook
            
        
        @python.observable("Orderbook", "Bid^{%(book)s}")
        def BidLastPrice(book = OfTrader())
             = LastPrice(Bids(book))
        
        @python.intrinsic.observable("Orderbook", "LastPrice(%(queue)s)", "orderbook.last_price._LastPrice_Impl")
        def LastPrice(queue = Asks()) : IObservable
            
        
        @python.observable("Orderbook", "Spread_{%(book)s}")
        def Spread(book = OfTrader())
             = AskPrice(book)-BidPrice(book)
        
        @python.intrinsic.observable("Orderbook", "LastTradePrice(%(queue)s)", "orderbook.last_trade._LastTradePrice_Impl")
        def LastTradePrice(queue = Asks()) : IObservable
            
    }
    
    package Moving {
        @python.intrinsic.function("Statistics", "Avg_{n=%(timeframe)s}(%(source)s)", "moments.ma.MA_Impl")
        def Avg(source = const(),
                timeframe = 100.0) : () => Float
            
        
        @python.intrinsic.function("Statistics", "\\sigma^2_{n=%(timeframe)s}(%(source)s)", "moments.mv.MV_Impl")
        def Var(source = const(),
                timeframe = 100.0)
             = Max(const(0.0),Avg(source*source,timeframe)-Sqr(Avg(source,timeframe)))
        
        @python.function("Statistics", "\\sqrt{\\sigma^2_{n=%(timeframe)s}_{%(source)s}}")
        def StdDev(source = const(),
                   timeframe = 100.0)
             = mathops.Sqrt(Var(source))
    }
    
    @python.intrinsic.observable("Basic", "[%(x)s]_dt=%(dt)s", "observable.on_every_dt._OnEveryDt_Impl")
    def OnEveryDt(dt = 1.0,
                  x = constant()) : IObservable
        
    
    @python.observable("Basic", "min{%(x)s, %(y)s}")
    def Min(x = constant(),
            y = constant())
         = if x<y then x else y
    
    @python.observable("RSI", "Downs_{%(timeframe)s}(%(source)s)")
    def DownMovements(source = orderbook.MidPrice(),
                      timeframe = 10.0)
         = Max(const(0.0),Lagged(source,timeframe)-source)
    
    @python.intrinsic.observable("Basic", "Lagged_{%(timeframe)s}(%(source)s)", "observable.lagged.Lagged_Impl")
    def Lagged(source = const(),
               timeframe = 10.0) : IObservable
        
    
    @python.observable("Basic", "max{%(x)s, %(y)s}")
    def Max(x = constant(),
            y = constant())
         = if x>y then x else y
    
    @python.observable("RSI", "Ups_{%(timeframe)s}(%(source)s)")
    def UpMovements(source = orderbook.MidPrice(),
                    timeframe = 10.0)
         = Max(const(0.0),source-Lagged(source,timeframe))
    
    @python.observable("Pow/Log", "{%(x)s}^2")
    def Sqr(x = constant())
         = x*x
    
    @python.observable("RSI", "RSI_{%(timeframe)s}^{%(alpha)s}(%(book)s)")
    def RSI(book = orderbook.OfTrader(),
            timeframe = 10.0,
            alpha = 0.015)
         = 100.0-100.0/(1.0+rsi.Raw(orderbook.MidPrice(book),timeframe,alpha))
}

package trash {
    package types {
        type T
        
        type R : T
        
        type U : T, R
        
        type T1 = T
    }
    
    package in1 {
        package in2 {
            def A(x = constant(),
                  y = if 3.0>x+2.0 then x else x*2.0) : () => types.T
                
        }
        
        def A(x : () => types.T1 = trash.A()) : () => types.U
            
    }
    
    def A(x = in1.in2.A()) : () => types.R
        
}

@python.function("Basic", "C=%(x)s")
def constant(x = 1.0) : IFunction
     = const(x)

type Side

type IOrderQueue

type IOrderBook

@python.intrinsic.function("Basic", "C=%(x)s", "_constant._Constant_Impl")
def const(x = 1.0) : IObservable
    

type ISingleAssetTrader

def Derivative(x : IDifferentiable = observable.EW.Avg()) : () => Float
    

type IDifferentiable : IFunction
