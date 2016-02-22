## A class for the cat.

from tkinter import *
import time

canvas = Canvas(width = 500, height = 500, bg = 'white')
canvas.pack()


class Cat:
    """ Class for the cat; i.e. the main character of the game..."""

    ## variable to record number of deaths.
    deaths = 0
        
    ## stuff to include: name, body...
    def __init__(self, name, catBody):
        self.name = name
        canvas.create_image(50, 10, image = catBody)

        ## Inventory list for items to be stored.
        self.inventory = []

    def body(self):
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

    def LeftKey(self,ID,nX,nY):
        try:
            if not self.canvas.coords(ID)[0] <= 0:
                self.canvas.move(ID, nX, nY)
        except:
            pass

    def RightKey(self,ID,nX,nY, canvasWidth):
        try:
            if not self.canvas.coords(ID)[0] >= canvasWidth-50:
                self.canvas.move(ID, nX, nY)
        except:
            pass
        
    def DownKey(self,ID,nX,nY, canvasHeight):
        try:
            if self.canvas.coords(ID)[1] < canvasHeight-50:
                self.canvas.move(ID, nX, nY)
        except:
            pass

    def UpKey(self,ID,nX,nY):
        try:
            if self.canvas.coords(ID)[1] > 0:
                self.canvas.move(ID, nX, nY)
        except:
            pass
        

    def movementBind(self):
        ##Link between keyboard keys and functions for movement.
        ## gui.root.bind
        canvas.bind('<Left>', Cat.LeftKey)
        canvas.bind('<Right>', Cat.RightKey)
        canvas.bind('<Up>', Cat.UpKey)
        canvas.bind('<Down>', Cat.DownKey)

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
