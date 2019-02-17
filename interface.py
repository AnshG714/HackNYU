from tkinter import *
from PIL import ImageTk,Image
import app
from app import *
import scanner
from scanner import *
import os

def init(data):
    data.x1 = data.width//4
    data.x2 = data.width*0.75
    data.y1 = data.height//2.8
    data.y2 = data.height//1.4
    data.camera = PhotoImage(file="/Users/sanja/Desktop/camera.gif")
    data.showImage = False
    data.rectLeft = data.width//2 + 72
    data.rectTop = data.height//2-60
    data.rectWidth = 36
    data.rectHeight = 25
    data.timerDelay = 100
    data.squareColor = "yellow"
    data.scannerReturns = []
def getUserInput():
    #get picture open camera and click a picture of a receipt

#This function takes x ad y coordinates from mousepress
#It changes the command based on the rectangle the mouse clicks
    pass

def mousePressed(event, data):
    if(data.x1<=event.x<=data.x2 and data.y1<=event.y<=data.y2):
        app.readPicture()
        data.showImage = True
    '''if(event.x< 150):
        index = 30*scanner.pricesOfE[data.priceNum] - 30
        if(<=event.y)'''

def keyPressed(event, data):
    pass
    
def timerFired(data):
    if data.squareColor == "yellow":
        data.squareColor = None
    else:
        data.squareColor = "yellow"




global receipt
def redrawAll(canvas, data):
    centerX = data.width//2
    centerY = data.height//2
    if(data.showImage == False):
        canvas.create_rectangle(0,0,data.width, data.height, fill = "cyan", width = 0)
        canvas.create_text(data.width//2, data.height//3.3, text = "Click to take a picture", font ="Chalkduster 25 bold")
        canvas.create_image(centerX, centerY, image=data.camera)
        canvas.create_rectangle(data.rectLeft,
                                    data.rectTop,
                                    data.rectLeft + data.rectWidth,
                                    data.rectTop + data.rectHeight,
                                    fill=data.squareColor)
    else:
        data.receipt = ImageTk.PhotoImage(Image.open('/Users/sanja/Desktop/rec_pics/opencv_frame_0.png'))
        canvas.create_image(centerX, centerY, image=data.receipt)
        canvas.create_text(data.width//3, data.height//6, text = "This is your receipt", fill="white", font = "Chalkduster 15 bold")
        for coord in range(len(scanner.coordinates)):
            canvas.create_rectangle(scanner.coordinates[coord][0], scanner.coordinates[coord][1], scanner.coordinates[coord][2], scanner.coordinates[coord][3], fill = None, outline="red", width=3,)
        i = 0
        for price in scanner.pricesOfE:
            textX = data.width//150
            margin = 30 # the whitespace from the top
            increment = 30 # how far apart each line should be printed
            canvas.create_text(textX, margin + increment*i, \
            text = price, anchor = 'w', fill = "gray",\
            font = "Arial 30" )
            i += 1


def runOurApp(width=500, height=500):

    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)
        
    def timerFiredWrapper(canvas, data):
            timerFired(data)
            redrawAllWrapper(canvas, data)
            # pause, then call timerFired again
            canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)

    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    root = Tk()
    root.title("Welcome to LikeGeeks app")
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    redrawAllWrapper(canvas, data)
    timerFiredWrapper(canvas, data)
    root.mainloop()  # blocks until window is closed
runOurApp()
