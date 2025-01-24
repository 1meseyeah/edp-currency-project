from events.event_base import Event

class PriceUpdateEvent(Event):
    event_name = "price_update"

    def __init__(self, symbol, price):
        payload = {"symbol": symbol, "price": price}
        super().__init__(payload)
