"""
Start doing stuff here!!!

TO DO:
The whole project :D

"""

from tkinter import *

def CleanSplit(string):
    """Splits strings at spaces and newlines
       used for spliting string that was read from txt file"""
    lPre = string.rsplit("\n") # l stands for list
    lFin = []

    for i in lPre:
        lFin.append(i.split())

    return lFin

def main():

    file = open("Map.txt","r")
    fList = CleanSplit(file.read())
    file.close()

    print(fList)

    window = Tk()
    window.title("Cat Hunt")

    wWidth = 250
    wHeight = 250
    Div = 50

    canvas = Canvas(window,width=wWidth, height=wHeight, bg="white")
    canvas.pack()

    for i in range(int(wHeight/Div)):
        for j in range(int(wWidth/Div)):
            x = j * Div
            y = i * Div
            if fList[i][j] == "1":
                Ob = canvas.create_rectangle(x, y, x + Div,y + Div, fill = "blue",outline = "blue")
            else:
                Ob = canvas.create_rectangle(x, y, x + Div,y + Div, fill = "Red",outline = "red")

    window.mainloop()

if __name__ == '__main__':
    main()
