import pyautogui as bot
import math 
import random 
import time 
import fishing
import mining 
import attacking
running = True

class Client: 
    def __init__(self, epoch=0, x_mark=[], world_switcher=[], inventory=[]):
        self.epoch = epoch 
        self.fisher = fishing.Fisher()
        self.miner = mining.Miner()
        self.attacker = attacking.Attacker() 

    def elapseTime(self):
        self.epoch = round(time.time() - self.epoch, 2)
        
client = Client()

training = ['fly fishing', 'net fishing', 'copper mining', 'coal mining', 'iron mining', 'trawler', 'minnows', 'attack rats', 'barbarian fishing']

train = input('What do you want to train? ') 
while train not in training:
    train = input('Not supported yet! What do you want to train? ')

while True: 
    if train == 'fly fishing':
        client.fisher.flyFishing()
    elif train == 'barbarian fishing':
        client.fisher.barbarianFishing()
    elif train == 'net fishing': 
        client.fisher.netFishing()
    elif train == 'minnows':
        client.fisher.minnows()
    elif train == 'copper mining':
        client.miner.mineCopper() 
    elif train == 'iron mining':
        client.miner.mineIron() 
    elif train == 'coal mining':
        client.miner.mineCoal() 
    elif train == 'trawler':
        client.fisher.trawler() 
    elif train == 'attack rats':
        client.attacker.rats()





