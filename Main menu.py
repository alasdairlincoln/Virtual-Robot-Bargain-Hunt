from tkinter import *
from tkinter import ttk



window = Tk()
#Title
title = Label(window, text= "CAT HUNT!", fg="blue",font = 'bold' )
title.pack()


#Empty frame for space

emptyframe1 = Frame(window).pack()
emptyLable1 = Label(emptyframe1).pack()

#inputing the cats name
frame1 = Frame(window)
frame1.pack( )

catnametext = Label(frame1,text="Cat name?", fg = "blue").pack(side = LEFT)
catname = Entry(frame1, fg = "blue").pack(side = LEFT)

#space 
emptyframe2 = Frame(window).pack()
emptyLable2 = Label(emptyframe2).pack()

#Different types of items

frame2 = Frame(window).pack()

lookfor = Label(frame2, text= "What do you wish to look for?", fg="blue").pack()
dropdown = StringVar(frame2)
dropdown.set("Cat Food") #defult opition
dropdown_1 = OptionMenu(frame2, dropdown,"Cat Food","Cat Toys","Mouse","Fish","coke")
dropdown_1.pack()
 
#space
emptyframe3 = Frame(window).pack()
emptyLable3 = Label(emptyframe3).pack()

#select difficutly
# This would be a bool opition "if true" then all we do
#is increase the speed of the dog moving around the room
diff = Label(window, text="Select a difficulty",fg="blue",font = 'bold').pack()
frame3 = Frame(window)
frame3.pack()

easy = Checkbutton(frame3, text="Pussy",fg="green").pack(side = LEFT,)# command =  bla bla
med = Checkbutton(frame3, text="Meh...better",fg="orange").pack(side = LEFT)# command =  bla bla
hard =Checkbutton(frame3, text="damn!",fg="red").pack(side = LEFT)# command =  bla bla

#space

emptyframe4 = Frame(window).pack()
emptyLable4 = Label(emptyframe4).pack()

#Start Button

startbutton = Button(window, text="PLAY!",font = 'bold',fg ='purple') #COMMAND = "The game funtion or class"
startbutton.pack()

#space
emptyframe5 = Frame(window).pack()
emptyLable5 = Label(emptyframe5).pack()

#audio/button

audiobutton = ttk.Button(window, text= "Audio").pack()





window.mainloop()
