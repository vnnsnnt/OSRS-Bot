import pyautogui as bot 
import time
mouseSpeed = 0.1

flyFishing = ['./fishImages/flyFishing.jpg', './fishImages/flyFishing2.jpg', './fishImages/flyFishing3.jpg']
netFishing = ['./fishImages/netFishing.jpg']
fullIndicator = './fishImages/fullIndicator.jpg'
levelUpIndicator = './clientImages/levelUpIndicator.jpg'
notFishing = './fishImages/notFishing.jpg'
inventoryOpen = './clientImages/inventoryOpen.jpg'
inventoryClosed = './clientImages/inventoryClosed.jpg'
inventorySalmon = './fishImages/inventorySalmon.jpg'
inventoryTrout = './fishImages/inventoryTrout.jpg'
inventoryShrimp = './fishImages/inventoryShrimp.jpg'
inventoryAnchovie = './fishImages/inventoryAnchovie.jpg' 
leakCue = './fishImages/leak.jpg'
net = './fishImages/net.jpg'
minnows = ['./fishImages/minnows1.jpg', './fishImages/minnows2.jpg', './fishImages/minnows3.jpg', './fishImages/minnows4.jpg', './fishImages/minnows5.jpg', './fishImages/minnows6.jpg']
barbarianFishing = ['./fishImages/barbarianFishing1.jpg', './fishImages/barbarianFishing2.jpg', './fishImages/barbarianFishing3.jpg', './fishImages/barbarianFishing4.jpg', './fishImages/barbarianFishing5.jpg' ]
inventoryLeapingTrout = './fishImages/inventoryLeapingTrout.jpg' 
inventoryLeapingSalmon = './fishImages/inventoryLeapingSalmon.jpg'
inventoryLeapingSturgeon = './fishImages/inventoryLeapingSturgeon.jpg'

class Fisher:
    def __init__(self, fishingSpot=[], isFishing=False, isFull=False, hasFishingSpot=False, currentFishing=[], fishes=[inventorySalmon, inventoryTrout]):
        self.fishingSpot = fishingSpot 
        self.isFishing = isFishing
        self.isFull = isFull 
        self.hasFishingSpot = hasFishingSpot 
        self.currentFishing = currentFishing 
        self.fishes = fishes
        self.isTrawling = False 
        self.interval = 0

    def calibrate(self): 
        if not self.isFishing: 
            if bot.locateOnScreen(fullIndicator, confidence=0.7) is not None: #check if inventory full 
                print('Full on fishes!') #if fullIndicator is found 
                self.isFull = True 
            elif bot.locateOnScreen(levelUpIndicator, confidence=0.7) is not None: #check if leveled up 
                bot.moveTo(bot.locateCenterOnScreen(levelUpIndicator, confidence=0.7)[0], bot.locateCenterOnScreen(levelUpIndicator, confidence=0.7)[1], mouseSpeed)
                bot.click() 
            else: 
                if bot.locateCenterOnScreen(inventoryOpen, confidence=0.9) is not None: 
                    bot.moveTo(bot.locateCenterOnScreen(inventoryOpen, confidence=0.6)[0], bot.locateCenterOnScreen(inventoryOpen, confidence=0.6)[1], mouseSpeed) 
                    bot.click() 
                print('Looking for a fishing spot!') 
                for images in self.currentFishing: 
                    print('trying image', images)
                    self.fishingSpot = bot.locateCenterOnScreen(images, confidence=0.6) #finds the fishing area
                    if self.fishingSpot is not None: #if fishing area is found 
                        print('Found a fishing spot!') 
                        self.hasFishingSpot = True 
                        break
                else: 
                    print('Failed to find a fishing spot!') 
                    
        
    def fish(self):
        self.calibrate() 
        if not self.isFishing and self.hasFishingSpot and not self.isFull and self.fishingSpot is not None: 
            bot.moveTo(self.fishingSpot[0], self.fishingSpot[1], mouseSpeed)
            bot.click() 
            self.isFishing = True 
            print('Started fishing!') 

        if self.isFishing:
            time.sleep(self.interval) #checks every for fishing on an interval 
            if bot.locateOnScreen(notFishing, confidence=0.6) is not None: 
                self.isFishing = False 
                print('Stopped fishing!') 
            
        if self.isFull: 
            print('Dropping inventory!')
            try:  
                if bot.locateCenterOnScreen(inventoryClosed, confidence=0.9) is not None:
                    bot.moveTo(bot.locateCenterOnScreen(inventoryClosed, confidence=0.8)[0], bot.locateCenterOnScreen(inventoryClosed, confidence=0.9)[1], mouseSpeed)
                    bot.click() 
            except: 
                pass
            bot.keyDown('shift') 
            for fish in self.fishes: 
                for item in bot.locateAllOnScreen(fish, confidence=0.85): 
                    bot.moveTo(item[0]+15, item[1]+15, mouseSpeed) 
                    bot.click() 
                print('Dropped all of %s' % fish)
            bot.keyUp('shift') 
            self.isFull = False 
        

    def flyFishing(self): 
        self.currentFishing = flyFishing 
        self.fishes = [inventorySalmon, inventoryTrout] 
        self.interval = 6
        self.fish()

    def netFishing(self):
        self.currentFishing = netFishing 
        self.fishes = [inventoryShrimp, inventoryAnchovie] 
        self.interval = 5
        self.fish() 
        
    
    def trawler(self):
        self.interval = 4
        if not self.isTrawling and bot.locateOnScreen(net, confidence=0.7) is None:
            self.fishingSpot = bot.locateCenterOnScreen(leakCue, confidence=0.8) 
            print('finding leak')
            if self.fishingSpot is not None: 
                bot.moveTo(self.fishingSpot[0], self.fishingSpot[1], 0.1)
                bot.click() 
                time.sleep(self.interval)
                self.isTrawling = False
            else:
                print('found no leak')

    def minnows(self):
        self.interval = 4
        self.currentFishing = minnows 
        self.fishes = [] 
        self.fish()

    def barbarianFishing(self):
        self.interval = 5
        self.currentFishing = barbarianFishing 
        self.fishes = [inventoryLeapingSalmon, inventoryLeapingTrout, inventoryLeapingSturgeon]
        self.fish()

    
        
