import pyautogui as bot
import math 
import random 
import time 
import fishing

#images
running = True
tick = 0.3

class Client: 
    def __init__(self, epoch=0, x_mark=[], world_switcher=[], inventory=[]):
        self.epoch = epoch 
        self.fisher = fishing.Fisher()

    def calibrate(self):
        pass

    def elapseTime(self):
        self.epoch = round(time.time() - self.epoch, 2)
        
client = Client()

while True: 
    time.sleep(tick)
    client.fisher.fish()
    client.calibrate()




