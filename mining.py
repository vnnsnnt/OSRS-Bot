import pyautogui as bot 
import time 

mouseSpeed = 0.3
copperMining = ['./mineImages/copperMining.jpg', './mineImages/copperMining2.jpg', './mineImages/copperMining3.jpg', './mineImages/copperMining4.jpg', './mineImages/copperMining5.jpg', './mineImages/copperMining6.jpg']
levelUpIndicator = './mineImages/levelUpIndicator.jpg' 
copperInventory = './mineImages/copperInventory.jpg' 
fullIndicator = './mineImages/fullIndicator.jpg'
inventoryOpen = './clientImages/inventoryOpen.jpg'
inventoryClosed = './clientImages/inventoryClosed.jpg' 
notMining = './mineImages/notMining.jpg'
inventoryCopper = './mineImages/inventoryCopper.jpg'
coalMining = ['./mineImages/coalMining.jpg', './mineImages/coalMining2.jpg', './mineImages/coalMining3.jpg', './mineImages/coalMining4.jpg', './mineImages/coalMining5.jpg']
ironMining = ['./mineImages/ironMining.jpg', './mineImages/ironMining2.jpg', './mineImages/ironMining3.jpg', './mineImages/ironMining4.jpg', './mineImages/ironMining5.jpg']
inventoryCoal = './mineImages/inventoryCoal.jpg'
inventoryIron = './mineImages/inventoryIron.jpg'


class Miner: 
    def __init__(self, miningSpot=[], isMining=False, isFull=False, hasMiningSpot=False, currentMining=copperMining, ores=[copperInventory]):
        self.miningSpot = miningSpot
        self.isMining = isMining 
        self.isFull = isFull 
        self.currentMining = currentMining 
        self.ores = ores
        self.hasMiningSpot = hasMiningSpot
        
    def calibrate(self):
        if not self.isMining:
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
                print('Looking for a mining spot!') 
                for images in self.currentMining:
                    print('trying', images)
                    self.miningSpot = bot.locateCenterOnScreen(images, confidence=0.55) #finds the mining area 
                    if self.miningSpot is not None: #if mining area is found 
                        print('Found a mining spot!') 
                        self.hasMiningSpot = True 
                        break 
                else:
                    print('Failed to find a mining spot!') 
                    
    def mine(self):
        self.calibrate() 
        if not self.isMining and self.hasMiningSpot and not self.isFull and self.miningSpot is not None:
            bot.moveTo(self.miningSpot[0], self.miningSpot[1], mouseSpeed) 
            bot.click() 
            self.isMining = True 
            print('Started Mining!') 
        
        if self.isMining: 
            time.sleep(1.9) #checks every for mining on an interval 
            if bot.locateOnScreen(notMining, confidence=0.6) is not None: 
                self.isMining = False 
                print('Stopped Mining!') 
            
        if self.isFull: 
            print('Dropping inventory!') 
            try: 
                if bot.locateCenterOnScreen(inventoryClosed, confidence=0.8) is not None: #if inventory is closed 
                    bot.moveTo(bot.locateCenterOnScreen(inventoryClosed, confidence=0.8)[0], bot.locateCenterOnScreen(inventoryClosed, confidence=0.8)[1], mouseSpeed) 
                    bot.click()
            except:
                pass 
            bot.keyDown('shift') 
            for ore in self.ores: 
                for item in bot.locateAllOnScreen(ore, confidence=0.85):
                    bot.moveTo(item[0]+15, item[1]+15, mouseSpeed) 
                    bot.click() 
                print('Dropped all of %s' % ore) 
            bot.keyUp('shift') 
            self.isFull = False 
        

    def mineCopper(self):
        self.currentMining = copperMining 
        self.ores = [inventoryCopper]
        self.mine()

    def mineIron(self): 
        self.currentMining = ironMining
        self.ores = [inventoryIron]
        self.mine()

    def mineCoal(self):
        self.currentMining = coalMining 
        self.ores = [inventoryCoal]
        self.mine()
