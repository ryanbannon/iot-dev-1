import dweepy
import time

def publish():
    dict = {}
    dict["publish"] = "true"
    dweepy.dweet_for('ryan-iot-dev-1', dict)

while True:
    publish()
    time.sleep(10)
