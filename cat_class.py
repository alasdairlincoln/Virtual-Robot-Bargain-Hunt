## A class for the cat.

from tkinter import *

canvas = Canvas(width = 300, height = 200, bg = 'white')
canvas.pack()

class Cat:
    """ Class for the cat; i.e. the main character of the game..."""

    deaths = 0
        
    ## stuff to include: name, body...
    def __init__(self, name):
        self.name = name

        self.inventory = []

    def body(b):
        image1 = PhotoImage(file = "Cat.png")
        canvas.create_image(50, 10, image = image1, anchor = NW)
        print("Body created")

    def death(c):
        ## Need dog code for this.
        print("You died")
        Cat.deaths = Cat.deaths + 1

    def itemPickUp(self, i):
        self.inventory.append(i)
        print(i + " added to inventory.")

    def itemDrop(self, d):
        self.inventory.remove(d)
        print(d + " dropped from inventory.")
        

cat = Cat("Cat")
cat.itemPickUp("food")
cat.itemPickUp("yarn")
cat.itemPickUp("milk")
cat.itemDrop("yarn")
cat.death()
print("Deaths: " + str(Cat.deaths))
        

mainloop()
