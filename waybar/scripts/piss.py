#!/usr/sbin/python3

from lightstreamer.client import LightstreamerClient, Subscription, SubscriptionListener

import time
import sys

class SimpleListener(SubscriptionListener):
    def __init__(self):
        self.value = None
        
    def onItemUpdate(self, item_update):
        self.value = item_update.getValue('Value')
        
    def onSubscriptionError(self, code, message):
        self.value = f"Error"

def main():
    client = LightstreamerClient(
        serverAddress='https://push.lightstreamer.com',
        adapterSet='ISSLIVE'
    )
    
    sub = Subscription(
        mode="MERGE",
        items=["NODE3000005"], # the urine tank
        fields=["Value", "Status"]
    )
    
    listener = SimpleListener()
    sub.addListener(listener)
    
    client.connect()
    client.subscribe(sub)

    while True:
        try:
            if listener.value:
                print(f'🧑🏽‍🚀🚽 {listener.value}%')
            else:
                print('🧑🏽‍🚀❗')
            sys.stdout.flush()
        except KeyboardInterrupt:
            client.unsubscribe(sub)
            client.disconnect()
            
        time.sleep(0.1)

if __name__ == '__main__':
    main()
