#Healthy Programmer
# 9am - 5pm
# Water - water.mp3 (3.5 litres) - Drank - log
# Eyes - eyes.mp3 - every 30 min - EyDone - log
# Physical activity - physical.mp3 every - 45 min - ExDone - log

import pygame
from time import time
from os import chdir

def getdate():
    from datetime import datetime
    return str(datetime.now())
date = getdate()

def music_loop(file, stopper):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while True:
        q = input()
        if q == stopper:
            pygame.mixer.music.stop()
            break

def log(txt):
    f = open('Hprog log.txt', 'a')
    txt_update = f"On {date}, {txt}\n"
    f.write(txt_update)
    f.close


if __name__ == "__main__":
    chdir(r"C:/Users/Admin/Documents/The-Leap")
    init_water = time()
    init_eyes = time()
    init_exercise = time()

    water_time = 30*60
    eyes_time = 20*60
    exercise_time = 45*60

    while True:
        if (time() - init_water) > water_time:
            print ("It's time to drink water! Write 'done' to stop the alarm.")
            music_loop('water.mp3', 'done')
            init_water = time()
            log("drank water")

        if (time() - init_eyes) > eyes_time:
            print ("It's time to relax your eyes! Write 'done' to stop the alarm.")
            music_loop('eyes.mp3', 'done')
            init_eyes = time()
            log("eyes relaxed")
            
        if (time() - init_exercise) > exercise_time:
            print ("It's time to exercise! Write 'done' to stop the alarm.")
            music_loop('exercise.mp3', 'done')
            init_exercise = time()
            log("got physical")
