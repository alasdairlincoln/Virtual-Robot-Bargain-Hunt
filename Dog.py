#from tkinter import *
import time
from math import sqrt

class Dog:
    
    def __init__(self,diff,gui,photo,Cat):
        """Difficulty,gui, photo of dog, cat"""
        self.diff = diff
        self.DogID = gui.CreateImageRectangle(photo,50,50,returnOn = True)

        self.x,self.y = gui.canvas.coords(self.DogID)

        # CAT / needs to be removed
        self.cat = Cat
        self.catID = Cat.catID
        self.UpdateCatCoords(gui) 

    def UpdateCatCoords(self,gui):
        self.cat_x,self.cat_y = gui.canvas.coords(self.catID)

    def distance(self):
        return sqrt( (self.cat_x-self.x)**2+(self.cat_y-self.y)**2 )
    
    def direction(self):
        d = self.distance()/4
        return (self.cat_x-self.x)/d, (self.cat_y-self.y)/d # tuple, 2D vector

    def move(self, vvx,vvy,gui):
        # something here causes errors when screen is changed or program is closed
        gui.canvas.move(self.DogID, vvx, vvy )
        self.x += vvx
        self.y += vvy
        
    def movement(self,gui):
                
        if self.diff == 1:
            vx = 5 # x velocity
            vy = 5 # y velocity
            # Boundaries
            x_min = 0
            y_min = 0
            x_max = 450
            y_max = 450
            
            x,y = gui.canvas.coords(self.DogID)
            
            # Move robot for 500 timesteps
            while True:
                self.UpdateCatCoords(gui)
                if x == self.cat_x and y == self.cat_y:
                    self.cat.death()
                    break
                else :
                    x,y = gui.canvas.coords(self.DogID)
                    
                    if x >= x_max:
                        vx = -5
                    if y <= y_min:
                        vy = 5
                    if y >= y_max:
                        vy = -5
                    if x <= x_min:
                        vx = 5
                    # Move dog
                    gui.canvas.move(self.DogID,vx,vy)
                    gui.canvas.update()  
                
                # Pause for 0.1 seconds, then delete the image
                time.sleep(0.1)

        if self.diff == 2:
            while True:
                self.UpdateCatCoords(gui)
                x,y= gui.canvas.coords(self.DogID)

                if y == self.cat_y and x ==self.cat_x:
                    self.cat.death()
                    break 
            
                elif y != self.cat_y:
                    if y < self.cat_y:
                        vy = 5
                    elif y > self.cat_y:
                        vy = -5

                    gui.canvas.move(self.DogID,0,vy)
                    gui.canvas.update()

                elif y == self.cat_y :
                    if x >= self.cat_x:
                        vx = -5
                    elif x <= self.cat_x:
                        vx = 5

                    gui.canvas.move(self.DogID,vx,0)
                    gui.canvas.update()
                
                time.sleep(0.05)            

        if self.diff == 3:
           
            while True:
                self.UpdateCatCoords(gui)
                if self.distance() > 20:
                    vvx,vvy = self.direction()
                    self.move(vvx,vvy,gui)
                else:
                    self.cat.death()
                    break

                gui.canvas.update()
               
                time.sleep(0.05)