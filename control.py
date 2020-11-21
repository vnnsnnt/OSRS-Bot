import pyautogui as bot
import math 
import random 
import time 
import fishing

running = True
tick = 0.3

class Client: 
    def __init__(self, epoch=0, x_mark=[], world_switcher=[], inventory=[]):
        self.epoch = epoch 
        self.fisher = fishing.Fisher()

    def elapseTime(self):
        self.epoch = round(time.time() - self.epoch, 2)
        
client = Client()

training = ['fly fishing', 'net fishing']

train = input('What do you want to train? ') 
while train not in training:
    train = input('Not supported yet! What do you want to train? ')

while True: 
    time.sleep(tick)
    if train == 'fly fishing':
        client.fisher.flyFishing()
    elif train == 'net fishing': 
        client.fisher.netFishing()
    





