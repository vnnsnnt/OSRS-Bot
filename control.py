import pyautogui as bot
import math 
import random 
import time 
from fishing import Fisher

#images
x_mark_area = './clientImages/x_mark.jpg'
world_switcher_area = './clientImages/world_switcher.jpg'
inventory_closed = './clientImages/inventory.jpg'
inventory_open = './clientImages/inventory_open.jpg' 

running = True
tick = 0.5

class Client: 
    def __init__(self, epoch=0, x_mark=[], world_switcher=[], inventory=[]):
        self.epoch = epoch 
        self.x_mark = x_mark
        self.world_switcher = world_switcher
        self.inventory = inventory
        self.fisher = Fisher()
    
    def calibrate(self):
        self.x_mark = bot.locateCenterOnScreen(x_mark_area, confidence=0.7)
        self.world_switcher = bot.locateCenterOnScreen(world_switcher_area, confidence=0.8)

    def elapseTime(self):
        self.epoch = round(time.time() - self.epoch, 2)
        
client = Client()

while True: 
    time.sleep(tick)
    client.fisher.fish()





