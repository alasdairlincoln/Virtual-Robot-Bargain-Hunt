import sys
from tkinter import *
from random import * # for random placement of houses 

# Import from our files
from TextureHandler import Textures
from Dog import Dog
from Cat import Cat

class GUI:

    def __init__(self,root):
        self.root = root
        self.frame = Frame(self.root)
        self.frame.pack()

        self.root.title("Cat Hunt")
       
    def CreateCanvas(self,wWidth = 500, wHeight = 500, Div = 50,background = "white"):
        self.canvas = Canvas(self.frame,width = wWidth,height = wHeight,bg = background)
        self.canvas.pack()
        self.Div = Div

    def CreateRectangle(self,x,y,Fill = "white",Outline = "black", returnOn = False):
        # Wrapper for create rectangle function
        rect = self.canvas.create_rectangle(x, y, x + self.Div,y + self.Div, fill = Fill,outline = Outline)
        self.canvas.pack()
        
        # Returns object ID
        if returnOn == True:
            return rect

    def CreateImageRectangle(self,photo,x,y,anch = NW,returnOn = False):
        """ Needs a loaded Photo .... """    
        imRect = self.canvas.create_image(x,y,image = photo,anchor = anch)
        self.canvas.pack()
        
        # Returns object ID
        if returnOn == True:
            return imRect

    def CreatCheckBox(self,frame,Text):
        check = IntVar()
        checkbox = Checkbutton(frame, text= Text, variable = check)
        checkbox.pack()
        
        return check

    def CreateEmptySpace(self, frame,x = 1, y = 5):
        space = Frame(frame)
        space.pack(padx = x, pady = y)

    def MoveObject(self,ID,X,Y):
        self.canvas.move(ID,X,Y)

    def ClearFrame(self):
        self.frame.destroy()
        self.frame = Frame(self.root)
        self.frame.pack()

class Map():
    def __init__(self,filePath):
        self.mapList = [] 
        self.ReadSplit(filePath)
        self.ExitX = 0
        self.ExitY = 0

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
                    gui.CreateImageRectangle(Textures.TextureDict["tree"],x,y)
                elif self.mapList[i][j] == "4":
                    gui.CreateImageRectangle(Textures.TextureDict["fenceH"],x,y)
                elif self.mapList[i][j] == "5":
                    gui.CreateImageRectangle(Textures.TextureDict["fenceV"],x,y)
                elif self.mapList[i][j] == "6":
                    gui.CreateImageRectangle(Textures.TextureDict["bush"],x,y)
                elif self.mapList[i][j] == "7":
                    gui.CreateImageRectangle(Textures.TextureDict["floor"],x,y)
                elif self.mapList[i][j] == "8":
                    gui.CreateImageRectangle(Textures.TextureDict["books"],x,y)
                elif self.mapList[i][j] == "9":
                    gui.CreateImageRectangle(Textures.TextureDict["table"],x,y)
                elif self.mapList[i][j] == "10":
                    gui.CreateImageRectangle(Textures.TextureDict["bed"],x,y)
                elif self.mapList[i][j] == "11":
                    gui.CreateImageRectangle(Textures.TextureDict["sofa"],x,y)
                    # add some kind of exit for outside
                    self.ExitX = x 
                    self.ExitY = y
                elif self.mapList[i][j] == "12":
                    gui.CreateImageRectangle(Textures.TextureDict["box"],x,y)    
                else:
                    raise ValueError("Unidentified symbol was found in MapList")       

    def Execute():
        print("BASE CLASS, shit went wrong OR u suck, @execute")

    def preChange():
        print("BASE CLASS, shit went wrong OR u suck, @change")

class mExterior(Map): # make into class like inside 
    def __init__(self, filePath):
        super().__init__(filePath)

    def Execute(self,gui,dMaps,dObjects):  
        gui.ClearFrame()
        gui.CreateCanvas()
        
        self.DisplayMap(gui)
        
        dObjects["houses"].CreateObjects(gui.canvas,5,"house","grass")
        dObjects["houses"].PlaceAllObjects(gui)

        cat = Cat(gui,Info.name,Textures.TextureDict["cat"],100,100)

        gui.root.bind("<Return>",lambda event: self.preChange(gui.canvas.coords(cat.catID),gui,dMaps,dObjects["houses"],dObjects)) # changes to inside map, <Return> is "enter" key

    def preChange(self,coords,gui,dMaps,House,dObjects): # move into one of the classes
        """Takes x,y coords in list,
           Checks if cat is standing on house and if yes proceeds to inside"""
        if not House.CheckOverlap(coords[0],coords[1]):
            dMaps["inside"].Execute(gui,dMaps,dObjects)

class mInterior(Map): # adapt for multiple instances
    def __init__(self, filePath):
        super().__init__(filePath)

    def Execute(self,gui,dMaps,dObjects):
        gui.ClearFrame()
        gui.CreateCanvas()

        self.DisplayMap(gui)
        
        dObjects["boxes"].CreateObjects(gui.canvas,5,"box","floor")
        dObjects["boxes"].PlaceItem()
        dObjects["boxes"].PlaceAllObjects(gui)

        cat = Cat(gui,Info.name,Textures.TextureDict["cat"],self.ExitX,self.ExitY)
        cat.itemPickUp(Item("asd",5))

        gui.root.bind("<Return>",lambda event: self.preChange(cat.catID,gui,dMaps,dObjects)) # changes to ouside map, <Return> is "enter" key

        dog = Dog(int(Info.difficulty),gui,Textures.TextureDict["dog"],cat)
        dog.movement(gui)

    def preChange(self,cat,gui,dMaps,dObjects):
        """changes into outside when on sofa only :D"""
        x,y = gui.canvas.coords(cat)
        if x == self.ExitX and y == self.ExitY:
            dMaps["outside"].Execute(gui,dMaps,dObjects)

class Obj:
    def __init__(self,x,y,texture):
        self.x = x
        self.y = y
        self.texture = texture
        self.ID = None

class BaseRandomObject:
    """Random object Base class"""
    def __init__(self):
        self.List = []

    def PlaceObject(self,gui,i):
        """places created object on tkinter canvas,
           requires gui"""
        self.List[i].ID = gui.CreateImageRectangle(self.List[i].texture,self.List[i].x,self.List[i].y,returnOn = True)

    def CreateObjects(self,canvas,amount,texture,chkImage):
        """Creates specified amount of objects"""
        
        while len(self.List) != amount:
            rInt = randint(1,100) 
            x,y = canvas.coords(rInt)
            currImage = canvas.itemcget(rInt,"image")
            #print(currImage)

            # Only place on specific tile and not overlap
            if currImage == Textures.TextStr(chkImage) and self.CheckOverlap(x,y):
                self.List.append(Obj(x,y,Textures.TextureDict[texture]))

    def CheckOverlap(self,x,y):
        """return true if none of current objects use the spot"""
        for h in self.List:
            if h.x == x and h.y == y:
                return False
        
        return True

    def PlaceAllObjects(self,gui):
        """places ALL created objects on tkinter canvas,
           uses PlaceObject method"""
        for i in range(len(self.List)):
            self.PlaceObject(gui,i)

class Item:
    def __init__(self,item,quality):
        """Enter item name, and quality int(1 being low quality, 5 being high quality) """
        self.item = item
        self.quality = quality

class Box(BaseRandomObject):
    def __init__(self):
       super().__init__()

       self.items = []

    def PlaceItem(self):
        # places item into the box randomly 
        while len(self.items) != len(self.List):
            rInt = randint(0,len(Info.availableItems)-1)
            rInt2 = randint(1,5)

            if Info.selectedItems[rInt]:
                self.items.append(Item(Info.availableItems[rInt],rInt2))
                print("placed: " + Info.availableItems[rInt] + " into the box")

    def GiveItem():
        # gives item to cat
        pass

class Info:
    name = ""
    difficulty = ""
    availableItems = ["Food","Toys","Mouse","Bells","Catnip","Milk","Trophy"]
    selectedItems = []

    def Transition(diffvar, catname, items,gui):
        for i in items:
            if i.get() == 1:
                Info.selectedItems.append(True)
            else:
                Info.selectedItems.append(False)

        Info.name = catname.get()
        Info.difficulty = diffvar.get()

        # Setup for rest of the program
        Textures.ReadTexture()

        dMaps = {}
    
        dMaps["outside"] = mExterior("Layouts/Outside Layout.txt")
        dMaps["inside"] = mInterior("Layouts/Inside Layout.txt")

        dObjects = {}
        dObjects["boxes"] = Box()
        dObjects["houses"] = BaseRandomObject()
    
        dMaps["outside"].Execute(gui,dMaps,dObjects)

def mainmenu(gui):
    #title
    title = Label(gui.frame, text= "CAT HUNT!", fg="blue",font = 'bold' )
    title.pack()

    gui.CreateEmptySpace(gui.frame)

    #inputing the cats name
    frame1 = Frame(gui.frame)
    frame1.pack( )

    catnametext = Label(frame1,text="Cat name?", fg = "blue").pack(side = LEFT)
    catname = Entry(frame1, fg = "blue")
    catname.pack(side = LEFT)
    
    gui.CreateEmptySpace(gui.frame)

    #Different types of items

    framebig =Frame(gui.frame)
    framebig.pack()
      
    lookfor = Label(framebig, text= "What do you wish to look for?", fg="blue")
    lookfor.pack()

    # adds a chechbox for every item in availableItems
    var = []
    for item in Info.availableItems:
        var.append(gui.CreatCheckBox(framebig,item))
    
    #select difficutly
    diffvar = IntVar()
        
    diff = Label(gui.frame, text="Select a difficulty",fg="blue", font = ("Arial",14))
    diff.pack()

    frame3 = Frame(gui.frame)
    frame3.pack()

    easy = Radiobutton(frame3, text = "Easy", fg = "green", variable = diffvar, value = 1)
    easy.pack(side = LEFT,)
    med = Radiobutton(frame3, text = "Medium", fg = "orange", variable = diffvar, value = 2)
    med.pack(side = LEFT)
    hard = Radiobutton(frame3, text = "Hard", fg = "red", variable = diffvar, value = 3)
    hard.pack(side = LEFT)

    gui.CreateEmptySpace(gui.frame)

    #Start Button
    startbutton = Button(gui.frame, text="PLAY!",font = ("Arial",14,"bold"),fg ='purple',command = lambda: Info.Transition(diffvar,catname,var,gui)) 
    startbutton.pack()

    gui.CreateEmptySpace(gui.frame)
    
def main():   
    # Setup tkinter
    root = Tk()
    gui = GUI(root)

    # To main menu and beyond
    mainmenu(gui)
    
    # Mainloop, MUST ALWAYS BE ON BOTTOM
    root.mainloop()
    
if __name__ == "__main__":
	sys.exit(main())
