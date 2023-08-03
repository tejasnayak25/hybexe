from modules.browser import createWindow
from modules.back import back
from modules.notification import notify

def func(data):
    back.send("Hi", "Hello from back!")

back.on(event="Bye", callback=func)




window = createWindow(title="HybExe", url="./src/index.html", resizable=True, draggable=True, text_select=True)

def start():
    # notify("Hello There", "Cool", "", 10)
    back.send("Bye", "Cool")

window.start(function=start, debug=True)