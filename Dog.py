from tkinter import *
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
        self.cat_x,self.cat_y = gui.canvas.coords(self.cat)

    def distance(self):
        return sqrt( (self.cat_x-self.x)**2+(self.cat_y-self.y)**2 )
    
    def direction(self):
        d = self.distance()/4
        return (self.cat_x-self.x)/d, (self.cat_y-self.y)/d # tuple, 2D vector

    def move(self, vvx,vvy,gui):
        gui.canvas.move(self.DogID, vvx, vvy )
        self.x += vvx
        self.y += vvy
        
    def movement(self,gui):
                
        if self.diff == 1:
            # The velocity, or distance moved per time step
            vx = 10.0 # x velocity
            vy = 5.0 # y velocity
            # Boundaries
            x_min = 0.0
            y_min = 0.0
            x_max = 450
            y_max = 450
            
            x,y = gui.canvas.coords(self.DogID)
            
            # Move robot for 500 timesteps
            while True:
                if x == self.cat_x and y == self.cat_y:
                    break
                    print("close")
                else :
                    #print(self.distance)
                    x,y = gui.canvas.coords(self.DogID)
                    #print(x,y)
                    #print(self.cat_x,self.cat_y)
                    
                    if x >= x_max:
                        vx = -10.0
                        
                    if y <= y_min:
                        vy = 5.0
                    if y >= y_max:
                        vy = -5.0
                    if x <= x_min:
                        vx = 10.0
                    # Move robot
                    gui.canvas.coords(self.DogID,x+vx,y+vy)
                    gui.canvas.update()  
                
                # Pause for 0.1 seconds, then delete the image
                time.sleep(0.1)

        if self.diff == 3:
           
            while True:
                if self.distance()>10:
                    vvx,vvy = self.direction()
                    #print( ":", self.x, self.y," -> ", self.x+vvx, self.y+vvy)
                    #print(self.x,self.y,self.distance())
                    #canvas.move(self.DogID, vvx, vvy )
                    self.move(vvx,vvy,gui)
                    #canvas.coords(self.DogID, self.x+vvx, self.y+vvy )
                    #print(self.x,self.y,self.distance())
                    #canvas.update()
                else:
                    print("close")
                    break

                gui.canvas.update()
               
                time.sleep(0.1)

        if self.diff == 2:
            x,y=gui.canvas.coords(self.DogID)

            while True:
                x,y= gui.canvas.coords(self.DogID)
                if y == self.cat_y and x ==self.cat_x:
                    print("close")
                    
                    break 
            
                elif y != self.cat_y:
                    
                    if y < self.cat_y:
                        vy = 5.0
                    elif y > self.cat_y:
                        vy = -5.0

                    gui.canvas.coords(self.DogID,x + 0,y + vy )
                    gui.canvas.update()

                elif y == self.cat_y :
                    if x >= self.cat_x:
                        vx = -10.0
                    elif x <= self.cat_x:
                        vx = 5.0

                    gui.canvas.coords(self.DogID,x + vx, y + 0)
                    gui.canvas.update()
                
                time.sleep(0.03)
                
                
"""root = Tk()
canvas = Canvas(root, width=400, height=300, bg='white')
canvas.pack(padx=10,pady=10)

photo2 = PhotoImage(file = "dog.png")
photo = PhotoImage(file = "dog.png")
dog =  Dog("easy", photo,photo2)            
dog.movement(photo)

root.mainloop()"""
