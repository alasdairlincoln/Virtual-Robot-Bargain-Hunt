"""
Start doing stuff here!!!

TO DO:
The whole project :D

"""

from tkinter import *

class cShop(): # c for Class

    def __init__(self,name,location,itemCount):
        self.name = name
        self.location = location
        self.itemCount = itemCount

    def __str__(self):
        return ("This shops name is: " + self.name + "\n" +
                "Location is: " + self.location + "\n" +
                "This shop has " + str(self.itemCount) +" items")

def main():

    window = Tk()
    window.title("Stuff")

    canvas = Canvas(window,width=400, height=400, bg="white")
    canvas.pack()

    Ob = canvas.create_rectangle(0,0,100,100,fill = "blue")

    Shop = cShop("Shitland","Uranus",20)

    print(Shop)

    window.mainloop()

if __name__ == '__main__':
    main()