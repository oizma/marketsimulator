
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
        def gammavariate(Alpha : Float = 1.0,
                         Beta : Float = 1.0) : () => Float
            
        
        /** Normal distribution
         */
        @python.random()
        def normalvariate(/** |mu| is the mean                  */ Mu : Float = 0.0,
                          /** |sigma| is the standard deviation */ Sigma : Float = 1.0) : () => Float
            
        
        /** Pareto distribution
         */
        @python.random()
        def paretovariate(/** |alpha| is the shape parameter*/ Alpha : Float = 1.0) : () => Float
            
        
        /** Triangular distribution
         *
         * Return a random floating point number *N* such that *low* <= *N* <= *high* and
         *       with the specified *mode* between those bounds.
         *       The *low* and *high* bounds default to zero and one.
         *       The *mode* argument defaults to the midpoint between the bounds,
         *       giving a symmetric distribution.
         */
        @python.random()
        def triangular(Low : Float = 0.0,
                       High : Float = 1.0,
                       Mode : Float = 0.5) : () => Float
            
        
        /** Von Mises distribution
         */
        @python.random()
        def vonmisesvariate(/** |mu| is the mean angle, expressed in radians between 0 and 2|pi|*/ Mu : Float = 0.0,
                            /** |kappa| is the concentration parameter, which must be greater than or equal to zero.
                              *      If |kappa| is equal to zero, this distribution reduces
                              *      to a uniform random angle over the range 0 to 2|pi|        */ Kappa : Float = 0.0) : () => Float
            
        
        /** Uniform distribution
         *
         * Return a random floating point number *N* such that
         * *a* <= *N* <= *b* for *a* <= *b* and *b* <= *N* <= *a* for *b* < *a*.
         * The end-point value *b* may or may not be included in the range depending on
         * floating-point rounding in the equation *a* + (*b*-*a*) * *random()*.
         */
        @python.random()
        def uniform(Low : Float = -10.0,
                    High : Float = 10.0) : () => Float
            
        
        /** Weibull distribution
         */
        @python.random()
        def weibullvariate(/** |alpha| is the scale parameter */ Alpha : Float = 1.0,
                           /** |beta| is the shape parameter  */ Beta : Float = 1.0) : () => Float
            
        
        /** Exponential distribution
         *
         *  Returned values range from 0 to positive infinity
         */
        @python.random()
        def expovariate(/** |lambda| is 1.0 divided by the desired mean. It should be greater zero.*/ Lambda : Float = 1.0) : () => Float
            
        
        /** Log normal distribution
         *
         * If you take the natural logarithm of this distribution,
         *  you'll get a normal distribution with mean |mu| and standard deviation |sigma|.
         *  |mu| can have any value, and |sigma| must be greater than zero.
         */
        @python.random()
        def lognormvariate(Mu : Float = 0.0,
                           Sigma : Float = 1.0) : () => Float
            
        
        /** Beta distribution
         *
         * Conditions on the parameters are |alpha| > 0 and |beta| > 0.
         * Returned values range between 0 and 1.
         */
        @python.random()
        def betavariate(Alpha : Float = 1.0,
                        Beta : Float = 1.0) : () => Float
            
    }
}

package mathops {
    /** Arc tangent of x, in radians.
     *
     */
    @python.mathops("Trigonometric", "atan", "atan(%(x)s)")
    def Atan(x : IFunction = constant(0.0)) : () => Float
        
    
    /** Square root of x
     *
     */
    @python.mathops("Log/Pow", "sqrt", "\\sqrt{%(x)s}")
    def Sqrt(x : IFunction = constant(1.0)) : () => Float
        
    
    /** Exponent of x
     *
     */
    @python.mathops("Log/Pow", "exp", "e^{%(x)s}")
    def Exp(x : IFunction = constant(1.0)) : () => Float
        
    
    /** Natural logarithm of x (to base e)
     *
     */
    @python.mathops("Log/Pow", "log", "log(%(x)s)")
    def Log(x : IFunction = constant(1.0)) : () => Float
        
    
    /** Return *x* raised to the power *y*.
     *
     * Exceptional cases follow Annex F of the C99 standard as far as possible.
     * In particular, ``pow(1.0, x)`` and ``pow(x, 0.0)`` always return 1.0,
     * even when *x* is a zero or a NaN.
     * If both *x* and *y* are finite, *x* is negative, and *y* is not an integer then
     * ``pow(x, y)`` is undefined, and raises ``ValueError``.
     */
    @python.mathops("Log/Pow", "pow", "%(base)s^{%(power)s}")
    def Pow(base : IFunction = constant(1.0),
            power : IFunction = constant(1.0)) : () => Float
        
}

package observable {
    package trader {
        @python.intrinsic.function("Proxies", "N/A", "trader.proxy._Single_Impl")
        def SingleProxy() : ISingleAssetTrader
            
    }
    
    package orderbook {
        def PriceAtVolume(queue : IOrderQueue = observable.orderbook.Asks(),
                          volume : Float = 100.0) : () => Float
            
        
        def WeightedPrice(queue : IOrderQueue = observable.orderbook.Asks(),
                          alpha : Float = 0.015) : () => Float
            
            	 = observable.EWMA(observable.orderbook.LastTradePrice(queue)*observable.orderbook.LastTradeVolume(queue),alpha)/observable.EWMA(observable.orderbook.LastTradeVolume(queue),alpha)
        
        def TickSize(book : IOrderBook = observable.orderbook.OfTrader()) : () => Float
            
        
        @python.observable("Orderbook", "MidPrice")
        def MidPrice(book : IOrderBook = observable.orderbook.OfTrader()) : () => Float
            
            	 = (observable.orderbook.AskPrice(book)+observable.orderbook.BidPrice(book))/2.0
        
        @python.intrinsic.function("Queue's", "Asks(%(book)s)", "orderbook.queue._Asks_Impl")
        def Asks(book : IOrderBook = observable.orderbook.OfTrader()) : IOrderQueue
            
        
        @python.observable("Orderbook", "Ask_{%(book)s}")
        def AskPrice(book : IOrderBook = observable.orderbook.OfTrader()) : () => Float
            
            	 = observable.orderbook.BestPrice(observable.orderbook.Asks(book))
        
        def LastTradeVolume(queue : IOrderQueue = observable.orderbook.Asks()) : IObservable
            
        
        @python.observable("Orderbook", "Bid^{%(book)s}")
        def BidPrice(book : IOrderBook = observable.orderbook.OfTrader()) : () => Float
            
            	 = observable.orderbook.BestPrice(observable.orderbook.Bids(book))
        
        @python.intrinsic.function("Queue's", "Bids(%(book)s)", "orderbook.queue._Bids_Impl")
        def Bids(book : IOrderBook = observable.orderbook.OfTrader()) : IOrderQueue
            
        
        @python.intrinsic.observable("Orderbook", "Price(%(queue)s)", "orderbook.props._BestPrice_Impl")
        def BestPrice(queue : IOrderQueue = observable.orderbook.Asks()) : IObservable
            
        
        @python.intrinsic.function("Proxies", "N/A", "orderbook.of_trader._OfTrader_Impl")
        def OfTrader(Trader : ISingleAssetTrader = observable.trader.SingleProxy()) : IOrderBook
            
        
        @python.intrinsic.observable("Orderbook", "LastPrice(%(queue)s)", "orderbook.props._LastPrice_Impl")
        def LastPrice(queue : IOrderQueue = observable.orderbook.Asks()) : IObservable
            
        
        @python.observable("Orderbook", "Spread")
        def Spread(book : IOrderBook = observable.orderbook.OfTrader()) : () => Float
            
            	 = observable.orderbook.AskPrice(book)-observable.orderbook.BidPrice(book)
        
        def LastTradePrice(queue : IOrderQueue = observable.orderbook.Asks()) : IObservable
            
    }
    @python.observable("Pow/Log", "{%(x)s}^2")
    def Sqr(x : IFunction = constant()) : () => Float
        
        	 = x*x
    
    @python.observable("Basic", "min{%(x)s, %(y)s}")
    def Min(x : IFunction = constant(),
            y : IFunction = constant()) : () => Float
        
        	 = if x<y then x else y
    
    @python.observable("Basic", "max{%(x)s, %(y)s}")
    def Max(x : IFunction = constant(),
            y : IFunction = constant()) : () => Float
        
        	 = if x>y then x else y
    
    @python.intrinsic.function("Statistics", "Avg_{\\alpha=%(alpha)s}(%(source)s)", "observable.ewma.EWMA_Impl")
    def EWMA(source : IObservable = const(),
             alpha : Float = 0.015) : () => Float
        
}

package trash {
    package types {type T
        type R : trash.types.T
        type U : trash.types.T, trash.types.R
        type T1 = trash.types.T
    }
    
    package in1 {
        package in2 {
            def A(x : IFunction = constant(),
                  y : IFunction = if 3.0>x+2.0 then x else x*2.0) : () => trash.types.T
                
        }
        def A(x : () => trash.types.T1 = trash.A()) : () => trash.types.U
            
    }
    def A(x : () => trash.types.T = trash.in1.in2.A()) : () => trash.types.R
        
}type IOrderQueue
type IOrderBook
type IObservable : IFunction
type IFunction = () => Float
type ISingleAssetTrader
@python.intrinsic.function("Basic", "C=%(x)s", "_constant._Constant_Impl")
def const(x : Float = 1.0) : IObservable
    

@python.function("Basic", "C=%(x)s")
def constant(x : Float = 1.0) : IFunction
    
    	 = const(x)
