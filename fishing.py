import pyautogui as bot 
import time
import math 
import random
tick = 0.3
shrimp_area = './fishImages/shrimp_area.jpg'
net_item = './fishImages/net.jpg'
is_fishing_cue = './fishImages/is_fishing.jpg'
full_cue = './fishImages/full_fishes.jpg'
not_fishing_cue = './fishImages/not_fishing.jpg'
inventory_closed = './clientImages/inventory.jpg'
inventory_open = './clientImages/inventory_open.jpg' 

class Fisher:
    def __init__(self, fishingSpot={}, tool=[], isFishing=False, isFull=False, hasFishingSpot=False):
        self.fishingSpot = fishingSpot
        self.tool = tool 
        self.isFishing = isFishing
        self.isFull = isFull 
        self.hasFishingSpot = hasFishingSpot
        self.isInventoryOpen = False 
    
    def calibrate(self):
        if not self.isFishing:
            if bot.locateOnScreen(full_cue, confidence=0.7) is not None: 
                print('Full on fishes!')
                self.isFull = True 
            else:
                inventory_area = bot.locateOnScreen(inventory_open, confidence=0.95) 
                if inventory_area is not None: 
                    bot.moveTo(inventory_area[0], inventory_area[1], tick)
                    bot.click()
                    self.isInventoryOpen = False 
                print('Looking for a fishing spot!')
                self.fishingSpot['spot'] = bot.locateCenterOnScreen(shrimp_area, confidence=0.7)
                if self.fishingSpot['spot'] is not None:
                    print('Found a fishing spot!') 
                    self.hasFishingSpot = True
                else:
                    print('Failed to find a fishing spot!')
        
    def fish(self): 
        self.calibrate()
        if not self.isFishing and self.hasFishingSpot and not self.isFull:
            bot.moveTo(self.fishingSpot['spot'][0], self.fishingSpot['spot'][1], tick)
            bot.click() 
            self.isFishing = True 
            print('Started Fishing') 
        if self.isFishing: 
            time.sleep(7)
            if bot.locateOnScreen(not_fishing_cue, confidence=0.7) is not None:
                self.isFishing = False 
                print('Stopped Fishing!')
        if self.isFull: 
            pass
            

            
           
