import time
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(
            title ="Alert!!!",
            message ="Do a python project everyday and more research on health care assistant in UK",
            timeout = 10
        )
        time.sleep(3600)