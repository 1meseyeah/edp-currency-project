from events.trade_events import TradeOrderEvent
from events.notification_events import TradeNotificationEvent
from event_dispatcher import EventDispatcher

class Trader:    
    def __init__(self, trader_id, dispatcher: EventDispatcher):
        self.trader_id = trader_id
        self.dispatcher = dispatcher
        self.stop_loss_orders = {}
        self.dispatcher.register_listener("trade_notification", self.receive_notification)
        self.dispatcher.register_listener("price_update", self.check_stop_loss)

    def place_order(self, symbol, quantity, order_type):
        print(f"[Trader {self.trader_id}] Placed {quantity} {symbol} {order_type.upper()} order.")
        event = TradeOrderEvent(self.trader_id, symbol, quantity, order_type)
        self.dispatcher.dispatch(event)

    def set_stop_loss(self, symbol, stop_price, quantity):
        self.stop_loss_orders[symbol] = {"stop_price": stop_price, "quantity": quantity}
        print(f"[Trader {self.trader_id}] Stop-Loss set: Selling {quantity} {symbol} if price drops to {stop_price} USD!")

    def check_stop_loss(self, payload):
        symbol = payload["symbol"]
        price = payload["price"]

        if symbol in self.stop_loss_orders and price <= self.stop_loss_orders[symbol]["stop_price"]:
            quantity = self.stop_loss_orders[symbol]["quantity"]
            print(f"[Trader {self.trader_id}] STOP-LOSS TRIGGERED: Selling {quantity} {symbol} at {price} USD!")
            self.place_order(symbol, quantity, "sell")
            del self.stop_loss_orders[symbol]

    def receive_notification(self, payload):
        if payload["trader_id"] == self.trader_id:
            print(f"[Trader {self.trader_id}] NOTIFICATION: {payload['message']}")
