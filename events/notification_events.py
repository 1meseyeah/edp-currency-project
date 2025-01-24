from events.event_base import Event

class TradeNotificationEvent(Event):
    event_name = "trade_notification"

    def __init__(self, trader_id, message):
        payload = {"trader_id": trader_id, "message": message}
        super().__init__(payload)
