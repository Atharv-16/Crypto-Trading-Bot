import requests
import time
import timeit
from plyer import notification
from datetime import datetime
data = requests.get('https://api.wazirx.com/api/v2/tickers')
prices = data.json()



#NOTIFIER
    def a(t,me):
        if __name__ == "__main__":
            notification.notify(
                title=t,
                message=me,

                # displaying time
                timeout=2
        )


