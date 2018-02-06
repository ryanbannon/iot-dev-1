import dweepy
from grovepi import *
import time

led = 8

pinMode(led,"OUTPUT")
time.sleep(1)

for dweet in dweepy.listen_for_dweets_from('ryan-iot-dev-1'):
    while True:
        try:
            digitalWrite(led,1)
            time.sleep(3)
            digitalWrite(led,0)

    
            
