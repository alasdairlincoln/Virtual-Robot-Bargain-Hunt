import sys
from tkinter import *

"""Discuss the further development of the program
   Should we make a wrapper for most of the stuff we use, or just the main stuff that is going to be needed for sure like canvas for map...
   I feel like create rectangle and other shapes that will be in the game is needed since we need to make the rectangles the same size
   the button is not rly needed... after much thinking
   move object is good, needs more wrapper layer to respond to button presses and move accordingly
   root should not be used, put everything into the frame which is acuired with gui.GetMainFrame()"""

"""Tasks:
   Make W/A/S/D or arrow keys move the cat
   Make cat class
   join implement main menu"""

class GUI:

    def __init__(self,root):
        self.__root = root
        self.__frame = Frame(self.__root).pack()

        # change window info here!
        self.__root.title("Cat Hunt")
        self.__wWidth = 500
        self.__wHeight = 500
        self.__Div = 50
        # ------------------------

        # Insert start/main menu here? make it return some stuff to here?

        # Canvas for map
        self.__canvas = Canvas(self.__frame,width = self.__wWidth, height = self.__wHeight, bg = "white")
        self.__canvas.pack()

    def CreateRectangle(self,x,y,Fill = "white",Outline = "black", returnOn = False):
        # Wrapper for create rectangle function
        rect = self.__canvas.create_rectangle(x, y, x + self.__Div,y + self.__Div, fill = Fill,outline = Outline)
        self.__canvas.pack()
        
        # in case the ractangle as an object its needed else where
        if returnOn == True:
            return rect

    def __ActionSelect(self,number,pArgs):
        # used as a place holder to get other commands, since i failed to pass in a command :| + google suggested this :D 
        if number == 0:
            # default case in case nothing specified
            pass
        elif number == 1:
            # unpack and pass arguments 
            ID = pArgs[0]
            x = pArgs[1]
            y = pArgs[2]
            self.MoveObject(ID,x,y)

    def CreateButton(self, txt, ComN = 0, comArgs = (), Side = "top", returnOn = False):
        button = Button(self.__frame,text = txt,command = lambda: self.__ActionSelect(ComN,comArgs))
        button.pack(side = Side)

        if returnOn == True:
            return button
    def MoveObject(self,ID,nX,nY):
            # use in conjunction with CreateRectangle with ReturnOn to get ID 
            self.__canvas.coords(ID, nX, nY, nX + self.__Div, nY + self.__Div,)
            self.__canvas.update()

    def GetWInfo(self):
        # returns window info since they are private
        return self.__wWidth, self.__wHeight, self.__Div

    def GetCanvas(self):
        return self.__canvas

    def GetMainFrame(self):
        return self.__frame

def ReadSplit(filePath):
    """Opens specified file, reads it and splits into single symbols"""

    # Read and close
    file = open(filePath,"r")
    string = file.read()
    file.close()
    # --------------

    # Splitting
    Pre = string.rsplit("\n")
    Final = []

    for i in Pre:
        Final.append(i.split())
    # ---------

    return Final

def DisplayMap(gui,mapList):
    # for ease of use
    wData = gui.GetWInfo()
    w = wData[0]
    h = wData[1]
    d = wData[2]
    # ---------------

    # Places all the rectangles
    for i in range(int(h / d)):
        y = i * d
        for j in range(int(w / d)):
            x = j * d
            
            if mapList[i][j] == "1":
                gui.CreateRectangle(x,y,"gray","gray")
            elif mapList[i][j] == "2":
                gui.CreateRectangle(x,y,"green","green")
            elif mapList[i][j] == "3":
                gui.CreateRectangle(x,y,"red","red")
            elif mapList[i][j] == "4":
                gui.CreateRectangle(x,y,"blue","blue")
            else:
                raise ValueError("Unidentified symbol was found in MapList")

def main():

    # Setup GUI
    root = Tk()
    gui = GUI(root) # DO NOT USE root past this point
    # ---------

    # Reads and displays map
    mapList = ReadSplit("Map.txt")
    DisplayMap(gui,mapList)
    # ----------------------

    # Make cat into class(OOP)
    cat = gui.CreateRectangle(100,100,"orange","orange",True)
    gui.CreateButton("Move",1,(cat,0,0))

    # Mainloop, MUST ALWAYS BE ON BOTTOM
    root.mainloop()
    
if __name__ == "__main__":
	sys.exit(main())