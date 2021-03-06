import sys
sys.path.append(r'../..')

from marketsim._pub import (strategy, trader, order, constant, event, math, orderbook)

const = constant

from common import expose

@expose("Trend Follower", __name__)
def TrendFollower(ctx):

    V = 1
    alpha = 0.015
    ctx.volumeStep = 30

    linear_signal = math.RandomWalk(initialValue=200,
                                      deltaDistr=const(-1), 
                                      name="200-t")
    
    demo = ctx.addGraph('demo')
    myVolume = lambda: [(orderbook.OfTrader().MidPrice, demo),
                        (trader.Position(), demo),
                        (orderbook.OfTrader().MidPrice.EW().Avg.OnEveryDt(1), demo)]

    return [
            ctx.makeTrader_A(
                strategy.price.LiquidityProvider()
                              .Strategy(orderFactory =
                                            order.side_price.Limit(volume=constant(V*8)).sideprice_WithExpiry(constant(100))),
                             label="liquidity"),
    
            ctx.makeTrader_A(strategy.side.Signal(linear_signal)
                                          .Strategy(event.Every(constant(1.)),
                                                    order.side.Market(const(V*3))),
                            "signal", 
                            [
                             (linear_signal, ctx.amount_graph)
                            ]),

            ctx.makeTrader_A(strategy.side.TrendFollower(alpha)
                                          .Strategy(event.Every(constant(1.)),
                                                    order.side.Market(volume = const(V))),
                             "trendfollower_ex",
                             myVolume()),
    ]
