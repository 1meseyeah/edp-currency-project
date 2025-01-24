from events.price_events import PriceUpdateEvent
from event_dispatcher import EventDispatcher
import random

class Exchange:    
    def __init__(self, dispatcher: EventDispatcher):
        self.dispatcher = dispatcher

    def update_price(self, symbol):
        """Updates the cryptocurrency price."""
        price = round(random.uniform(100, 500), 2)
        print(f"[Exchange] {symbol} price updated: {price} USD")
        event = PriceUpdateEvent(symbol, price)
        self.dispatcher.dispatch(event)
