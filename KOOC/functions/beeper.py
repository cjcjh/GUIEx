from cs1robots import *
import time

load_world("../worlds/beeper1.wld")
hubo = Robot()
sleep_time = 0.5

def move_and_pick():
    time.sleep(sleep_time)
    hubo.move()
    if hubo.on_beeper():
        time.sleep(sleep_time)
        hubo.pick_beeper()

for i in range(9):
    move_and_pick()
