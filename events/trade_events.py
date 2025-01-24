from events.event_base import Event

class TradeOrderEvent(Event):
    event_name = "trade_order"

    def __init__(self, trader_id, symbol, quantity, order_type):
        payload = {
            "trader_id": trader_id,
            "symbol": symbol,
            "quantity": quantity,
            "order_type": order_type
        }
        super().__init__(payload)

class TradeExecutedEvent(Event):
    event_name = "trade_executed"

    def __init__(self, trader_id, symbol, quantity, price, order_type):
        payload = {
            "trader_id": trader_id,
            "symbol": symbol,
            "quantity": quantity,
            "price": price,
            "order_type": order_type
        }
        super().__init__(payload)
