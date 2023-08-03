from modules.back import back
        
def send(event, message):
    if not back.find(event):
        back.pushMessage(event=event, message=message)
    messageReceived(event=event)
    
def messageReceived(event):
    back.call(event=event)