import os
import led_hat
from time import sleep
from datetime import datetime
while True:
    ct=datetime.now()
    try:
        os.lstat('/dev/input/event1')
        
    except FileNotFoundError:
        print(ct)
        led_hat.red()
        print('BLUETOOTH NOT CONNECTED')
        sleep(.25)
        led_hat.green()
        sleep(.25)
    else:
        print(ct)
        print('CONNECTED')
        led_hat.cleanup()
    sleep(.25)
    
    
