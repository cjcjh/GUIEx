from cs1robots import *
import time

load_world("../worlds/beeper1.wld")
hubo = Robot()
sleep_time = 0.5


while not hubo.on_beeper():
    time.sleep(sleep_time)
    hubo.move()
