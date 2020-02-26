from cs1robots import *
import time

create_world(avenues = 5, streets = 5)
hubo = Robot()
sleep_time = 0.5

def move_or_turn():
    if hubo.front_is_clear():
        time.sleep(sleep_time)
        hubo.move()
    else:
        time.sleep(sleep_time)
        hubo.turn_left()

for i in range(20):
    move_or_turn()
