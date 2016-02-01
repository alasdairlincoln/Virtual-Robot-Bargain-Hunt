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

    def CreateImageRectangle(self,photo,x,y,anch):
        """ Needs a loaded Photo .... """    
        self.__canvas.create_image(x,y,image = photo,anchor = anch)
        self.__canvas.pack()

    def MoveObject(self,ID,nX,nY):
        # use in conjunction with CreateRectangle with ReturnOn to get ID 
        self.__canvas.coords(ID, nX, nY, nX + self.__Div, nY + self.__Div,)
        self.__canvas.update()

    def Callback(self,event):
        print("pressed " + str(event.keycode))

    def GetWInfo(self):
        # returns window info since they are private
        return self.__wWidth, self.__wHeight, self.__Div

    def GetCanvas(self):
        return self.__canvas

    def GetMainFrame(self):
        return self.__frame

    def ClearFrame(self):
        # As name suggests, cleats the main frame
        self.__frame.destroy()
        self.__frame = Frame(self.__root)
        self.__frame.pack()

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

def DisplayMap(gui,mapList,h,w,d):

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

    mainCanvasWidth = 500
    mainCanvasHeight = 500
    mainCanvasDiv = 50

    # Setup GUI
    root = Tk()
    gui = GUI(root) # DO NOT USE root past this point
    gui.CreateCanvas(mainCanvasWidth,mainCanvasHeight,mainCanvasDiv,"black")
    # ---------

    # Reads and displays map
    #mapList = ReadSplit("Map.txt")
    #DisplayMap(gui,mapList,mainCanvasWidth,mainCanvasHeight,mainCanvasDiv)
    # ----------------------

    # Make cat into class(OOP)
    cat = gui.CreateRectangle(100,100,"orange","orange",True)
    frame = gui.GetMainFrame()
    button = Button(frame,text = "Move",command = lambda: gui.MoveObject(cat,0,0))
    button.pack()

    root.bind("<KeyRelease>",gui.Callback)
    frame.pack()

    photo = PhotoImage(file = "asd.png")
    gui.CreateImageRectangle(photo,0,0,NW)

    # Mainloop, MUST ALWAYS BE ON BOTTOM
    root.mainloop()
    
if __name__ == "__main__":
	sys.exit(main())