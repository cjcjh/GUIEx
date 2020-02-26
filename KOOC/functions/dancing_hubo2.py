from cs1robots import *
import time

create_world(avenues = 3, streets = 3)
hubo = Robot(beepers = 10)
sleep_time = 0.5

def dance():
    for i  in range(4):
        time.sleep(sleep_time)
        hubo.turn_left()

def move_or_turn():
    if hubo.front_is_clear():
        dance()
        time.sleep(sleep_time)
        hubo.move()
    else:
        time.sleep(sleep_time)
        hubo.turn_left()
    time.sleep(sleep_time)
    hubo.drop_beeper()

for i in range(18):
    move_or_turn()
