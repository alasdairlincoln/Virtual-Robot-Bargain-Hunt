import sys
from tkinter import *
from random import * # for random placement of houses 

class GUI:

    def __init__(self,root):
        self.root = root
        self.frame = Frame(self.root)
        self.frame.pack()

        self.root.title("Cat Hunt")
       
    def CreateCanvas(self,wWidth = 500, wHeight = 500, Div = 50,background = "white"):
        # Creates Canvas
        self.canvas = Canvas(self.frame,width = wWidth,height = wHeight,bg = background)
        self.canvas.pack()
        self.Div = Div

    def CreateRectangle(self,x,y,Fill = "white",Outline = "black", returnOn = False):
        # Wrapper for create rectangle function
        rect = self.canvas.create_rectangle(x, y, x + self.Div,y + self.Div, fill = Fill,outline = Outline)
        self.canvas.pack()
        
        # in case the ractangle as an object its needed else where
        if returnOn == True:
            return rect

    def CreateImageRectangle(self,photo,x,y,anch = NW,returnOn = False):
        """ Needs a loaded Photo .... """    
        imRect = self.canvas.create_image(x,y,image = photo,anchor = anch)
        self.canvas.pack()
        
        if returnOn == True:
            return imRect

    def MoveObject(self,ID,X,Y):
        """Moves object"""
        self.canvas.move(ID,X,Y)

    # all of this should be in cat class
    # and use MoveObject from this class
    def LeftKey(self,ID,nX,nY):
        self.canvas.move(ID, nX, nY)

    def RightKey(self,ID,nX,nY):
        self.canvas.move(ID, nX, nY)
        
    def DownKey(self,ID,nX,nY):
        self.canvas.move(ID, nX, nY)

    def UpKey(self,ID,nX,nY):
        self.canvas.move(ID, nX, nY)
    # ---------------------------

    def ClearFrame(self):
        # As name suggests, cleats the main frame
        self.frame.destroy()
        self.frame = Frame(self.root)
        self.frame.pack()

class Textures():
    TextureDict = {} # DICTIONARY POWAAHHH!

    def ReadTexture():
        """ Loads textures that are used in game
            USE ONCE ONLY """

        Textures.TextureDict["grass"] = PhotoImage(file = "Textures/grass.png")
        Textures.TextureDict["path"] = PhotoImage(file = "Textures/path.png")
        Textures.TextureDict["cat"] = PhotoImage(file = "Textures/cat.png")
        Textures.TextureDict["house"] = PhotoImage(file = "Textures/House.png")
        Textures.TextureDict["a"] = PhotoImage(file = "Textures/pc1.png")
        Textures.TextureDict["b"] = PhotoImage(file = "Textures/pc2.png")

    def GetTextureKeys():
        return Textures.TextureDict.keys()

class Map():
    def __init__(self,filePath):
        self.mapList = [] 
        self.ReadSplit(filePath)

    def ReadSplit(self,filePath):
        """Reads the map and places into 2D array/list,
           no returns, puts it directly into class"""

        file = open(filePath,"r")
        string = file.read()
        file.close()

        Pre = string.rsplit("\n")

        for i in Pre:
            self.mapList.append(i.split())

    def DisplayMap(self,gui,h = 500, w = 500, d = 50):

        for i in range(int(h / d)):
            y = i * d
            for j in range(int(w / d)):
                x = j * d
                
                #add more elif for more options

                if self.mapList[i][j] == "1":
                    gui.CreateImageRectangle(Textures.TextureDict["grass"],x,y)
                elif self.mapList[i][j] == "2":
                    gui.CreateImageRectangle(Textures.TextureDict["path"],x,y)
                elif self.mapList[i][j] == "3":
                    gui.CreateImageRectangle(Textures.TextureDict["a"],x,y)
                elif self.mapList[i][j] == "4":
                    gui.CreateImageRectangle(Textures.TextureDict["b"],x,y)
                else:
                    raise ValueError("Unidentified symbol was found in MapList")

    def Execute():
        print("BASE CLASS, shit went wrong OR u suck, @execute")

    def preChange():
        print("BASE CLASS, shit went wrong OR u suck, @change")

class mExterior(Map): # make into class like inside 
    def __init__(self, filePath):
        super().__init__(filePath)
        self.hNR = 5 # number of houses in game

    def Execute(self,gui,dMaps):       
        gui.ClearFrame()
        gui.CreateCanvas()
        
        self.DisplayMap(gui)
        House.CreateHouses(gui.canvas,self.hNR)  
        House.PlaceHouses(gui)


        # Make cat into class(OOP)
        # all of this should be in cat class
        Cat = gui.CreateImageRectangle(Textures.TextureDict["cat"],100,100,returnOn = True)

        gui.root.bind("<Left>", lambda event: gui.LeftKey(Cat,-50,0))
        gui.root.bind("<Right>", lambda event: gui.RightKey(Cat,50,0))
        gui.root.bind("<Up>", lambda event: gui.UpKey(Cat,0,-50))
        gui.root.bind("<Down>", lambda event: gui.DownKey(Cat,0,50))
        # -------------------------

        gui.root.bind("<Return>",lambda event: self.preChange(gui.canvas.coords(Cat),gui,dMaps)) # changes to inside map 
        # <Return> is "enter" key

    def preChange(self,coords,gui,dMaps): # move into one of the classes
        """Takes x,y coords in list,
           Checks if cat is standing on house and if yes proceeds to inside"""
        if not House.CheckOverlap(coords[0],coords[1]):
            dMaps["inside"].Execute(gui,dMaps)

class mInterior(Map): # adapt for multiple instances
    def __init__(self, filePath):
        super().__init__(filePath)

    def Execute(self,gui,dMaps):
        gui.ClearFrame()
        gui.CreateCanvas()

        self.DisplayMap(gui)

        gui.root.bind("<Return>",lambda event: self.preChange(gui,dMaps)) # changes to ouside map
        # <Return> is "enter" key

    def preChange(self,gui,dMaps):
        """PLACE HOLDER FOR NOW, goes to another map"""
        dMaps["outside"].Execute(gui,dMaps)

class House():
    """If used via CreateHouses then
       It contains list of itself"""
    HouseList = []

    def __init__(self,x,y,texture):
        self.x = x
        self.y = y
        self.texture = texture
        self.ID = None

    def CreateHouses(canvas,amount):
        """Creates specified amount of houses"""

        while len(House.HouseList) != amount:
            rInt = randint(1,100) 
            x,y = canvas.coords(rInt)
            currImage = canvas.itemcget(rInt,"image")

            # place only on grass and not on another house
            if currImage == "pyimage1" and House.CheckOverlap(x,y):
                House.HouseList.append(House(x,y,Textures.TextureDict["house"]))

    def CheckOverlap(x,y):
        """return true if none of current houses use the spot"""
        for h in House.HouseList:
            if h.x == x and h.y == y:
                return False

        return True

    def PlaceHouses(gui):
        """places created houses on tkinter canvas,
           requires gui because it uses its function"""
        for h in House.HouseList:
            h.ID = gui.CreateImageRectangle(h.texture,h.x,h.y,NW,True)

def main():   
    # Setup
    root = Tk()
    gui = GUI(root) 

    Textures.ReadTexture()

    dMaps = {}

    ## add other maps here
    dMaps["outside"] = mExterior("Layouts/Outside Layout.txt")
    dMaps["inside"] = mInterior("Layouts/Inside Layout.txt")
    # ---------

    # Main Stuff
    dMaps["outside"].Execute(gui,dMaps)
    # ----------

    # Mainloop, MUST ALWAYS BE ON BOTTOM
    root.mainloop()
    
if __name__ == "__main__":
	sys.exit(main())