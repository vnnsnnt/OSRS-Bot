import pyautogui as bot
import math 
import random 
import time 
import fishing
import mining 
running = True
tick = 0.3

class Client: 
    def __init__(self, epoch=0, x_mark=[], world_switcher=[], inventory=[]):
        self.epoch = epoch 
        self.fisher = fishing.Fisher()
        self.miner = mining.Miner()

    def elapseTime(self):
        self.epoch = round(time.time() - self.epoch, 2)
        
client = Client()

training = ['fly fishing', 'net fishing', 'copper mining', 'coal mining', 'iron mining']

train = input('What do you want to train? ') 
while train not in training:
    train = input('Not supported yet! What do you want to train? ')

while True: 
    time.sleep(tick)
    if train == 'fly fishing':
        client.fisher.flyFishing()
    elif train == 'net fishing': 
        client.fisher.netFishing()
    elif train == 'copper mining':
        client.miner.mineCopper() 
    elif train == 'iron mining':
        client.miner.mineIron() 
    elif train == 'coal mining':
        client.miner.mineCoal() 
    





