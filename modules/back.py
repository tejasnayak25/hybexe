class Back:
    def __init__(self):
        self.messages = []
        self.events = []
        self.window = None
        
    def send(self, event, message):
        self.window.evaluate_js(f'window.receiver("{event}", "{message}");')
        return
        
    def pushMessage(self, event, message):
        self.messages.append({ "event": event, "message": message })
        return

    def on(self, event, callback):
        self.events.append({ "event": event, "callback": callback })
        return
    
    def find(self, event):
        for message in self.messages:
            if message["event"] == event:
                return message
            else: 
                continue
        return False
    
    def findCall(self, event):
        for savedEvent in self.events:
            if savedEvent["event"] == event:
                return savedEvent["callback"]
            else: 
                continue
        return False
    
    def call(self, event):
        for message in self.messages:
            if message["event"] == event:
                callback = self.findCall(event=event)
                data = message["message"]
                if not callback:
                    return False
                callback(data)
                return
            else: 
                continue
        return False
    
    
back = Back()