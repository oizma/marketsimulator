class IEvent(object):
    def LiquidityProviderSide(self, orderFactory = None,side = None,initialValue = None,priceDistr = None):
        from marketsim.gen._out.strategy._liquidityproviderside import LiquidityProviderSide
        return LiquidityProviderSide(self,orderFactory,side,initialValue,priceDistr)
    
    def LiquidityProvider(self, orderFactory = None,initialValue = None,priceDistr = None):
        from marketsim.gen._out.strategy._liquidityprovider import LiquidityProvider
        return LiquidityProvider(self,orderFactory,initialValue,priceDistr)
    
    pass
