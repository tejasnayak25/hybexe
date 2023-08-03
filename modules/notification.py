from plyer import notification

def notify(title, message, app_icon, timeout):
    notification.notify(
        title = title,
        message = message,
        app_icon = app_icon,
        timeout = timeout
    )
    return