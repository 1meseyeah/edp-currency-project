from event_dispatcher import EventDispatcher
from agents.exchange import Exchange
from agents.trader import Trader
from agents.trade_engine import TradeEngine

dispatcher = EventDispatcher()

exchange = Exchange(dispatcher)
trader = Trader("Trader_1", dispatcher)
trade_engine = TradeEngine(dispatcher)

exchange.update_price("BTC")

trader.place_order("BTC", 2, "buy")

trader.set_stop_loss("BTC", 250, 2)

exchange.update_price("BTC")

trade_engine.show_trade_history()