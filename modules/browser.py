import webview
from modules.modules import send
from modules.back import back
    
class createWindow:
    def __init__(self, title = "Example Project", url = None, html = None, js_api = None, width = 800, height = 600, x = None, y = None, resizable = False, fullscreen = False, min_size = (200, 100), hidden = False, frameless = False, easy_drag = True, focus = True, minimized = False, on_top = False, confirm_close = False, background_color = "#FFFFFF", transparent = False, text_select = False, zoomable = False, draggable = False, vibrancy = False, localization = None, http_port = None, server_args = {}):
        self.window = webview.create_window(title=title, url=url, html=html, js_api=js_api, width=width, height=height, x=x, y=y, resizable=resizable, fullscreen=fullscreen, min_size=min_size, hidden=hidden, frameless=frameless, easy_drag=easy_drag, focus=focus, minimized=minimized, on_top=on_top, confirm_close=confirm_close, background_color=background_color, transparent=transparent, text_select=text_select, zoomable=zoomable, draggable=draggable, vibrancy=vibrancy, localization=localization, http_port=http_port, server_args=server_args)
        self.window.expose(send)
        back.window = self.window
        
        
    def start(self, function = None, args = None, localization={}, gui=None, debug=False, http_server=False, http_port=None, user_agent=None, private_mode=True, storage_path=None, menu=[], server_args={}, ssl=False):
        webview.start(func=function, args=args, localization=localization, gui=gui, debug=debug, http_server=http_server, http_port=http_port, user_agent=user_agent, private_mode=private_mode, storage_path=storage_path, menu=menu, server_args=server_args, ssl=ssl)

    # Create a webview window
    

    # Start the webview main loop

# if __name__ == "__main__":
#     main()
