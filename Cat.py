from TextureHandler import Textures

class Cat:
    """ Class for the cat; i.e. the main character of the game..."""

    deaths = 0
          
    def __init__(self, gui, name, catBody,x,y):
        self.name = name
        self.catID = gui.CreateImageRectangle(catBody,x,y,returnOn = True)
        self.movementBind(gui)

        self.inventory = []

    def death(self):
        Cat.deaths += 1
        print(self.name + " #" + str(Cat.deaths) +" died")
        
        # add game over? add item drop?       

    def itemPickUp(self, Item):
        # Item should be a class Item
        # Takes item
        self.inventory.append(Item)
        print(Item.item + ", quality: " + str(Item.quality) + " added to inventory.")

    def itemDrop(self, Item):
        # Item should be a class Item
        # Drops item
        self.inventory.remove(Item)
        print(Item.item + ", quality: " + str(Item.quality) + " dropped from inventory.")

    def movementBind(self,gui):
        # Link between keyboard keys and functions for movement.
        gui.root.bind("<Left>", lambda event: self.LeftKey(gui,-50,0))
        gui.root.bind("<Right>", lambda event: self.RightKey(gui,50,0,500))
        gui.root.bind("<Up>", lambda event: self.UpKey(gui,0,-50))
        gui.root.bind("<Down>", lambda event: self.DownKey(gui,0,50,500))

    def CheckAhead(self,gui,x,y):
        """Prevents from walking on fences and trees"""
        cX,cY = gui.canvas.coords(self.catID)

        cX += x
        cY += y

        ground = gui.canvas.itemcget(gui.canvas.find_overlapping(cX,cY,cX+50,cY+50)[0],"image")

        if not ground == Textures.TextStr("tree") and \
           not ground == Textures.TextStr("fenceH") and \
           not ground == Textures.TextStr("fenceV"):
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