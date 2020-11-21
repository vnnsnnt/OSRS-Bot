import pyautogui as bot 
import time
mouseSpeed = 0.3

flyFishing = ['./fishImages/flyFishing.jpg', './fishImages/flyFishing2.jpg', './fishImages/flyFishing3.jpg']
netFishing = ['./fishImages/netFishing.jpg']
fullIndicator = './fishImages/fullIndicator.jpg'
levelUpIndicator = './fishImages/levelUpIndicator.jpg'
notFishing = './fishImages/notFishing.jpg'
inventoryOpen = './fishImages/inventoryOpen.jpg'
inventoryClosed = './fishImages/inventoryClosed.jpg'
inventorySalmon = './fishImages/inventorySalmon.jpg'
inventoryTrout = './fishImages/inventoryTrout.jpg'
inventoryShrimp = './fishImages/inventoryShrimp.jpg'
inventoryAnchovie = './fishImages/inventoryAnchovie.jpg' 

class Fisher:
    def __init__(self, fishingSpot=[], isFishing=False, isFull=False, hasFishingSpot=False, currentFishing=flyFishing, fishes=[inventorySalmon, inventoryTrout]):
        self.fishingSpot = fishingSpot 
        self.isFishing = isFishing
        self.isFull = isFull 
        self.hasFishingSpot = hasFishingSpot 
        self.currentFishing = currentFishing 
        self.fishes = fishes

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
            time.sleep(6) #checks every for fishing on an interval 
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
        self.fish()

    def netFishing(self):
        self.currentFishing = netFishing 
        self.fishes = [inventoryShrimp, inventoryAnchovie] 
        self.fish() 
    

