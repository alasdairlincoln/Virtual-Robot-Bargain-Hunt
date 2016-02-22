## A class for the cat.

from tkinter import *
import time

#canvas = Canvas(width = 500, height = 500, bg = 'white')
#canvas.pack()


class Cat:
    """ Class for the cat; i.e. the main character of the game..."""

    ## variable to record number of deaths.
    deaths = 0
        
    ## stuff to include: name, body...
    def __init__(self, gui, name, catBody,x,y):
        self.name = name
        self.catID = gui.CreateImageRectangle(catBody,x,y,returnOn = True)
        self.x = x # cat coords
        self.y = y
        self.movementBind(gui)

        ## Inventory list for items to be stored.
        self.inventory = []

    def body(self):
        # dafug is this ? does it have some intended stuff?
        print("Body created")

    def death(self):
        ## Need dog code for this.
        print("You died")
        Cat.deaths = Cat.deaths + 1

    def itemPickUp(self, i):
        ## When an item is picked up it is stored in the inventory list.
        self.inventory.append(i)
        print(i + " added to inventory.")

    def itemDrop(self, d):
        ## Items can be dropped from the list, this would be due to contact
        ## with the dog.
        self.inventory.remove(d)
        print(d + " dropped from inventory.")

    def LeftKey(self,ID,gui,nX,nY):
        try:
            if gui.canvas.coords(ID)[0] > 0:
                gui.MoveObject(ID, nX, nY)
        except:
            pass

    def RightKey(self,ID,gui,nX,nY, canvasWidth):
        try:
            if gui.canvas.coords(ID)[0] < canvasWidth-50:
                gui.MoveObject(ID, nX, nY)
        except:
            pass
        
    def DownKey(self,ID,gui,nX,nY, canvasHeight):
        try:
            if gui.canvas.coords(ID)[1] < canvasHeight-50:
                gui.MoveObject(ID, nX, nY)
        except:
            pass

    def UpKey(self,ID,gui,nX,nY):
        try:
            if gui.canvas.coords(ID)[1] > 0:
                gui.MoveObject(ID, nX, nY)
        except:
            pass
        
    def movementBind(self,gui):
        ##Link between keyboard keys and functions for movement.
        gui.root.bind("<Left>", lambda event: self.LeftKey(self.catID,gui,-50,0))
        gui.root.bind("<Right>", lambda event: self.RightKey(self.catID,gui,50,0,500))
        gui.root.bind("<Up>", lambda event: self.UpKey(self.catID,gui,0,-50))
        gui.root.bind("<Down>", lambda event: self.DownKey(self.catID,gui,0,50,500))
"""
## Velocity.
vx = 5.0
vy = 5.0
    
catBody = PhotoImage(file = "Textures/cat.png")

#test.
cat = Cat("Cat", catBody)
cat.body()
cat.itemPickUp("food")
cat.itemPickUp("yarn")
cat.itemPickUp("milk")
cat.itemDrop("yarn")
cat.death()

print(str(len(cat.inventory)) + " items in the inventory.")
print("Deaths: " + str(Cat.deaths))

mainloop()
"""