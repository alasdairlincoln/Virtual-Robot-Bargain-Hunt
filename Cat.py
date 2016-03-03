from TextureHandler import Textures
from Gui import GUI
from tkinter import *

class Cat:
    """ Class for the cat; i.e. the main character of the game..."""

    deaths = 0
    inventory = []
          
    def __init__(self, gui, name, catBody,x,y,box = None):
        self.name = name
        self.catID = gui.CreateImageRectangle(catBody,x,y,returnOn = True)
        self.CatKeyBinds(gui,box)

    def death(self):
        Cat.deaths += 1
        print(self.name + " #" + str(Cat.deaths) +" died")
        
        # add game over? add item drop?       

    def itemPickUp(self, Item):
        # takes item, the item should be class Item
        Cat.inventory.append(Item)
        print(str(Item)  + " added to inventory")

    def itemDrop(self, Item):
        # Drops item
        Cat.inventory.remove(Item)
        print(str(Item) + " dropped from inventory")

    def openBox(self,gui,box):
        try:
            cX, cY = gui.canvas.coords(self.catID)

            boxUnd, ID = box.CheckOverlap(cX,cY,True)
            if not boxUnd:
                self.itemPickUp(box.GiveItem(ID,gui))
        except:
            pass

    def SortItems(self,criteria,gui,gameover):
        sortList = self.inventory 
        if criteria == "quality":
            for i in range(len(sortList)):
                for j in range(len(sortList)):
                    if sortList[i].quality > sortList[j].quality:
                        tmp = sortList[i]
                        sortList[i] = sortList[j]
                        sortList[j] = tmp
        
        elif criteria == "name":
            for i in range(len(sortList)):
                for j in range(len(sortList)):
                    if sortList[i].item < sortList[j].item:
                        tmp = sortList[i]
                        sortList[i] = sortList[j]
                        sortList[j] = tmp

        gui.ClearFrame()
        self.showInventory(gui,GameOver = gameover)

    def showInventory(self,gui = None, GameOver = False):
        """Seperate window for score"""
        if gui == None:
            root = Tk()
            gui = GUI(root,"Inventory")

        if GameOver:
            label = Label(gui.frame,text = "Game over",fg = "red",font = ("Arial",16,"bold"))
            label.pack(padx = 100)

        label = Label(gui.frame,text = "Your cat has " + str(len(Cat.inventory)) + " items:")
        label.pack(padx = 100)

        for i in Cat.inventory:
            label = Label(gui.frame,text = str(i))
            label.pack(padx = 100)

        button = Button(gui.frame,text = "Sort by quality",command = lambda: self.SortItems("quality",gui,GameOver))
        button.pack(side = LEFT)
        button = Button(gui.frame,text = "Sort by name",command = lambda: self.SortItems("name",gui,GameOver))
        button.pack(side = RIGHT)

        if GameOver:
            button = Button(gui.frame,text = "Exit",fg = "red",font = ("Arial",14,"bold"),command = lambda: sys.exit())
            button.pack()

            gui.root.protocol("WM_DELETE_WINDOW",lambda:sys.exit()) 

        gui.root.mainloop

    def CatKeyBinds(self,gui,box):
        # All key bindings associated with Cat
        gui.root.bind("<Left>", lambda event: self.LeftKey(gui,-50,0))
        gui.root.bind("<Right>", lambda event: self.RightKey(gui,50,0,500))
        gui.root.bind("<Up>", lambda event: self.UpKey(gui,0,-50))
        gui.root.bind("<Down>", lambda event: self.DownKey(gui,0,50,500))
        gui.root.bind("<x>",lambda event: self.openBox(gui,box))
        gui.root.bind("<c>",lambda event: self.showInventory())

    def CheckAhead(self,gui,x,y):
        """Prevents from walking on fences and trees"""
        cX,cY = gui.canvas.coords(self.catID)

        cX += x
        cY += y

        ground = gui.canvas.itemcget(gui.canvas.find_overlapping(cX,cY,cX+50,cY+50)[0],"image")

        if not ground == Textures.TextStr("tree") and \
           not ground == Textures.TextStr("fenceH") and \
           not ground == Textures.TextStr("fenceV") and \
           not ground == Textures.TextStr("wall"):
            return True
        else:
            return False

    def LeftKey(self,gui,nX,nY):
        try:
            if gui.canvas.coords(self.catID)[0] > 0 and self.CheckAhead(gui,nX,nY):
                gui.MoveObject(self.catID, nX, nY)
        except:
            pass

    def RightKey(self,gui,nX,nY, canvasWidth):
        try:
            if gui.canvas.coords(self.catID)[0] < canvasWidth-50 and self.CheckAhead(gui,nX,nY):
                gui.MoveObject(self.catID, nX, nY)
        except:
            pass
        
    def DownKey(self,gui,nX,nY, canvasHeight):
        try:
            if gui.canvas.coords(self.catID)[1] < canvasHeight-50 and self.CheckAhead(gui,nX,nY):
                gui.MoveObject(self.catID, nX, nY)
        except:
            pass

    def UpKey(self,gui,nX,nY):
        try:
            if gui.canvas.coords(self.catID)[1] > 0 and self.CheckAhead(gui,nX,nY):
                gui.MoveObject(self.catID, nX, nY)
        except:
            pass