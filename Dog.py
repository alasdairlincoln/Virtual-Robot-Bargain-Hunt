from tkinter import *
import time
from math import sqrt

class Dog:
    
    def __init__(self,diff,photo,photo2):
        global canvas
        self.diff = diff
        
        self.id1= canvas.create_image(10,15,image = photo, anchor =  CENTER)
        self.x,self.y=canvas.coords(self.id1)
        self.cat = canvas.create_image(220,150, image = photo2, anchor = CENTER)
        self.cat_x,self.cat_y = canvas.coords(self.cat)

    def distance(self):
        return sqrt( (self.cat_x-self.x)**2+(self.cat_y-self.y)**2 )
    
    def direction(self):
        d = self.distance()/4
        return (self.cat_x-self.x)/d, (self.cat_y-self.y)/d # tuple, 2D vector
    def move(self, vvx,vvy):
        canvas.move(self.id1, vvx, vvy )
        self.x += vvx
        self.y += vvy
        
    def movement(self,photo):
        global canvas
        
        if self.diff == "easy":
            # The velocity, or distance moved per time step
            vx = 10.0 # x velocity
            vy = 5.0 # y velocity
            # Boundaries
            x_min = 0.0
            y_min = 0.0
            x_max = 350
            y_max = 250
            
            x,y = canvas.coords(self.id1)
            
            # Move robot for 500 timesteps
            for i in range(500):
                if x == self.cat_x and y == self.cat_y:
                    print("close")
                else :
                    print(self.distance)
                    x,y = canvas.coords(self.id1)
                    print(x,y)
                    print(self.cat_x,self.cat_y)
                    
                    if x >= x_max:
                        vx = -10.0
                        
                    if y <= y_min:
                        vy = 5.0
                    if y >= y_max:
                        vy = -5.0
                    if x <= x_min:
                        vx = 10.0
                    # Move robot
                    canvas.coords(self.id1,x+vx,y+vy)
                    canvas.update()  
                
                # Pause for 0.1 seconds, then delete the image
                time.sleep(0.1)

        if self.diff == "hard": # ============================================
           
            for i in range(500):
                if self.distance()>10:
                    vvx,vvy = self.direction()
                    #print( ":", self.x, self.y," -> ", self.x+vvx, self.y+vvy)
                    #print(self.x,self.y,self.distance())
                    #canvas.move(self.id1, vvx, vvy )
                    self.move(vvx,vvy)
                    #canvas.coords(self.id1, self.x+vvx, self.y+vvy )
                    #print(self.x,self.y,self.distance())
                    #canvas.update()
                else:
                    print("close")

                canvas.update()
               
                time.sleep(0.1)

        if self.diff == "medium":
            x,y=canvas.coords(self.id1)
            for i in range(500):
                x,y=canvas.coords(self.id1)
                if y == self.cat_y and x ==self.cat_x:
                    print("close")
            
                elif y != self.cat_y:
                    
                    if y < self.cat_y:
                        vy = 5.0
                    elif y > self.cat_y:
                        vy = -5.0
                    canvas.coords(self.id1,x + 0,y + vy )
                    canvas.update()
                elif y == self.cat_y :
                    if x >= self.cat_x:
                        vx = -10.0
                    elif x <= self.cat_x:
                        vx = 5.0
                    canvas.coords(self.id1,x + vx, y + 0)
                    canvas.update()
                
                time.sleep(0.03)
                
root = Tk()
canvas = Canvas(root, width=400, height=300, bg='white')
canvas.pack(padx=10,pady=10)
# Cat


# ---            
           
photo2 = PhotoImage(file = "dog.png")
photo = PhotoImage(file = "dog.png")
dog =  Dog("medium", photo,photo2)            
dog.movement(photo)
root.mainloop()
