import pyautogui as bot
import time
mouseSpeed = 0.2

ratAttacking = ['./attackImages/rat1.jpg', './attackImages/rat2.jpg', './attackImages/rat3.jpg', './attackImages/rat4.jpg', './attackImages/rat5.jpg', './attackImages/rat6.jpg', './attackImages/rat7.jpg', './attackImages/rat8.jpg']

class Attacker:
    def __init__(self, entityLocation=[], isAttacking=False, hasAgro=False, currentAttacking=ratAttacking, currentEntity=[]):
        self.entityLocation = entityLocation
        self.isAttacking = isAttacking
        self.hasAgro = hasAgro 
        self.currentAttacking = ratAttacking 
        self.currentEntity = currentEntity
        
    def calibrate(self):
        print('here')
        if True:
            print('Looking for enemy to attack!') 
            for images in self.currentAttacking:
                self.entityLocation = bot.locateCenterOnScreen(images, confidence=0.58) #finds the enemy 
                if self.entityLocation is not None: #if an enemy is found 
                    print('Found an enemy to attack!') 
                    self.hasAgro = True 
                    break 
            else:
                print('Failed to find an enemy to attack') 

    def attack(self):
        self.calibrate() 
        if not self.isAttacking and self.hasAgro and self.entityLocation is not None: 
            bot.moveTo(self.entityLocation[0], self.entityLocation[1], mouseSpeed)
            bot.click() 
            self.isAttacking = True 
            print('Started Attacking!') 
        
        if self.isAttacking:
            time.sleep(2) 
            if bot.locateOnScreen(self.currentEntity, confidence=0.6) is None: 
                self.isAttacking = False 
                print('Stopped attacking')
            
    def rats(self): 
        self.currentAttacking = ratAttacking 
        self.currentEntity = './attackImages/ratIndicator.jpg'
        self.attack()