import sys
from tkinter import *

def ReadSplit(filePath):
    """Opens specified file, reads it and splits into single symbols"""

    file = open(filePath,"r")
    string = file.read()
    file.close()

    lPre = string.rsplit("\n") # l stands for list
    lFinal = []

    for i in lPre:
        lFinal.append(i.split())

    return lFinal

class GUI:

    def __init__(self,root):
        self.__root = root

        # change window info here!
        self.__root.title("Cat Hunt")
        self.__wWidth = 250
        self.__wHeight = 250
        self.__Div = 50
        # ------------------------

        self.__canvas = Canvas(self.__root,width = self.__wWidth, height = self.__wHeight, bg = "white")
        self.__canvas.pack()

    def CreateRectangle(self,x,y,Fill = "white",Outline = "black", returnOn = False):
        # Wrapper for create rectangle function
        rect = self.__canvas.create_rectangle(x, y, x + self.__Div,y + self.__Div, fill = Fill,outline = Outline)
        self.__canvas.pack()
        
        # in case the ractangle as an object its needed else where
        if returnOn == True:
            return rect

    def __actionSelect(self,number,pArgs):
        # used as a place holder to get other commands, since i failed to pass in a command :| + google suggested this :D 
        if number == 0:
            # default case in case nothing specified
            pass
        if number == 1:
            # unpack and pass arguments 
            ID = pArgs[0]
            x = pArgs[1]
            y = pArgs[2]
            self.MoveObject(ID,x,y)

    def CreateButton(self, txt,ComN = 0,comArgs = ()):
        button = Button(self.__root,text = txt,command = lambda: self.__actionSelect(ComN,comArgs))
        button.pack()

        #add in return option like rectangle, for reasons ?

    def GetWInfo(self):
        # returns window info since they are private
        return (self.__wWidth,self.__wHeight,self.__Div)

    def MoveObject(self,ID,nX,nY):
        # use in conjunction with CreateRectangle with ReturnOn to get ID 
        self.__canvas.coords(ID, nX, nY, nX + self.__Div, nY + self.__Div,)
        self.__canvas.update()
    
def DisplayMap(gui,MapList):
    # for ease of use
    wData = gui.GetWInfo()
    w = wData[0]
    h = wData[1]
    d = wData[2]

    for i in range(int(h / d)):
        y = i * d
        for j in range(int(w / d)):
            x = j * d
            
            if MapList[i][j] == "1":
                gui.CreateRectangle(x,y,"gray","gray")
            elif MapList[i][j] == "2":
                gui.CreateRectangle(x,y,"green","green")
            elif MapList[i][j] == "3":
                gui.CreateRectangle(x,y,"red","red")
            else:
                raise ValueError("Unidentified symbol was found in MapList")

def main():

    root = Tk()
    gui = GUI(root)

    MapList = ReadSplit("Map.txt")
    
    DisplayMap(gui,MapList)

    # make cat into class go with OOP (object oriented programing)
    Cat = gui.CreateRectangle(100,100,"orange","orange",True)
    gui.CreateButton("Move",1,(Cat,0,0))

    root.mainloop()

if __name__ == "__main__":
	sys.exit(main())