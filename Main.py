import sys
from tkinter import *
from random import * # for random placement of houses 

class GUI:

    def __init__(self,root):
        self.__root = root
        self.__frame = Frame(self.__root)
        self.__frame.pack()

        self.__root.title("Cat Hunt")
       
    def CreateCanvas(self,wWidth,wHeight,Div,background = "white"):
        # Creates Canvas
        self.__canvas = Canvas(self.__frame,width = wWidth,height = wHeight,bg = background)
        self.__canvas.pack()
        self.__Div = Div


    def CreateRectangle(self,x,y,Fill = "white",Outline = "black", returnOn = False):
        # Wrapper for create rectangle function
        rect = self.__canvas.create_rectangle(x, y, x + self.__Div,y + self.__Div, fill = Fill,outline = Outline)
        self.__canvas.pack()
        
        # in case the ractangle as an object its needed else where
        if returnOn == True:
            return rect

    def CreateImageRectangle(self,photo,x,y,anch = NW,returnOn = False):
        """ Needs a loaded Photo .... """    
        image = self.__canvas.create_image(x,y,image = photo,anchor = anch)
        self.__canvas.pack()

        if returnOn == True:
            return image

    def MoveObject(self,ID,X,Y):
        """Moves object,
           doesn't require canvas ouside :)"""
        self.__canvas.move(ID,X,Y)

    def LeftKey(self,ID,nX,nY):
        self.__canvas.move(ID, nX, nY)

    def RightKey(self,ID,nX,nY):
        self.__canvas.move(ID, nX, nY)
        
    def DownKey(self,ID,nX,nY):
        self.__canvas.move(ID, nX, nY)

    def UpKey(self,ID,nX,nY):
        self.__canvas.move(ID, nX, nY)

    def GetCanvas(self):
        return self.__canvas

    def GetMainFrame(self):
        return self.__frame

    def ClearFrame(self):
        # As name suggests, cleats the main frame
        self.__frame.destroy()
        self.__frame = Frame(self.__root)
        self.__frame.pack()

class eTextures():
    """Enum for map textures,
       Simplyfies the acces of textures, names instead of number"""
    grass = 0
    path = 1
    cat = 2
    house = 3

class Map():
    def __init__(self):
        self.mapList = []
        self.mapTextures = []    
        
        self.ReadTextures() 

    def ReadTextures(self):
        """Loads textures that are used in game"""

        # add each texture ad the end of list and add another variable in class eTextures
        self.mapTextures.append(PhotoImage(file = "Textures/grass.png"))
        self.mapTextures.append(PhotoImage(file = "Textures/path.png"))
        self.mapTextures.append(PhotoImage(file = "Textures/cat.png"))
        self.mapTextures.append(PhotoImage(file = "Textures/House.png"))

        #print(self.mapTextures)

    def ReadSplit(self,filePath):
        """Reads the map and places into 2D array/list,
           No returns, puts it directly into class"""

        # Read and close
        file = open(filePath,"r")
        string = file.read()
        file.close()
        # --------------

        # Splitting
        Pre = string.rsplit("\n")

        for i in Pre:
            self.mapList.append(i.split())

    def DisplayMap(self,gui,h,w,d):

        for i in range(int(h / d)):
            y = i * d
            for j in range(int(w / d)):
                x = j * d
                
                #add more elif for more options

                if self.mapList[i][j] == "1":
                    gui.CreateImageRectangle(self.mapTextures[eTextures.grass],x,y)
                elif self.mapList[i][j] == "2":
                    gui.CreateImageRectangle(self.mapTextures[eTextures.path],x,y)
                else:
                    raise ValueError("Unidentified symbol was found in MapList")

    def PlaceHouse(self,gui, amount, start = False):
        if start:
            amount -= 1

        canvas = gui.GetCanvas()

        rInt = randint(1,100) 
        x,y = canvas.coords(rInt)

        currImage = canvas.itemcget(rInt,"image")
        #print(canvas.itemcget(rInt,"image") + " " + str(rInt))
        #print(type(canvas.itemcget(rInt,"image")))


        # place only on grass, whitelisting grass, some other might be later
        if currImage == "pyimage1":
            house = gui.CreateImageRectangle(self.mapTextures[eTextures.house],x,y,NW,True)
            if amount > 0:
                self.PlaceHouse(gui,amount - 1)
        else:
            self.PlaceHouse(gui,amount)

def main():

    mainCanvasWidth = 500
    mainCanvasHeight = 500
    mainCanvasDiv = 50

    # Setup GUI
    root = Tk()
    gui = GUI(root) # DO NOT USE root past this point, GET MAIN FRAME

    
    gui.CreateCanvas(mainCanvasWidth,mainCanvasHeight,mainCanvasDiv,"black")
    # ---------

    # Reads and displays map
    map = Map()
    mapList = map.ReadSplit("Map.txt")
    map.DisplayMap(gui,mainCanvasWidth,mainCanvasHeight,mainCanvasDiv)
    map.PlaceHouse(gui,2,True) # change the number to change the number of houses
    # ----------------------

    # Make cat into class(OOP)
    Cat = gui.CreateImageRectangle(map.mapTextures[eTextures.cat],100,100,returnOn = True)
    frame = gui.GetMainFrame()

    button = Button(frame,text = "Move",command = lambda: gui.MoveObject(Cat,50,50))
    button.pack()

    root.bind("<Left>", lambda event: gui.LeftKey(Cat,-5,0))
    root.bind("<Right>", lambda event: gui.RightKey(Cat,5,0))
    root.bind("<Up>", lambda event: gui.UpKey(Cat,0,-5))
    root.bind("<Down>", lambda event: gui.DownKey(Cat,0,5))

    # Mainloop, MUST ALWAYS BE ON BOTTOM
    root.mainloop()
    
if __name__ == "__main__":
	sys.exit(main())