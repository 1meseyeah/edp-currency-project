class Event:
    def __init__(self, payload=None):
        self.payload = payload if payload else {}

    @property
    def event_name(self):
        raise NotImplementedError("Subclasses must define event_name!")
