#In the future this file will be used to edit/configurate settings
#Right now all it does is display the live hand tracking, which visualises the backend of the project.

print("HandUI is loading. Please wait...")

import tkinter
from landmarker import Landmarker;
from PIL import Image, ImageTk

class App:
    def __init__(self, title, height, width):
        self.window = tkinter.Tk()
        self.window.title(title)

        self.canvas = tkinter.Canvas(self.window, width = width, height = height)
        self.canvas.pack()

        self.createMenu()

        self.displayHandTrackingButton = tkinter.Button(self.window, text="Toggle hand tracking visualiser", command=self.displayVisualiser)
        self.displayHandTrackingButton.pack()
        self.displayHandTracking = False

        self.centerPointText_dev = self.canvas.create_text((200,10),text="Center Point:", fill='black')

        self.lm = Landmarker(True)

        self.lm.recordCam()
        self.update()

        self.window.mainloop()

    def createMenu(self):

        menu = tkinter.Menu(self.window)
        self.window.config(menu=menu)



    def update(self):

        self.canvas.itemconfig(self.centerPointText_dev, text=f"Center point: {self.lm.boxCenter} ---- Frame dimensions (hxw): {self.lm.frameHeight}, {self.lm.frameWidth}")

        #display tracking visualiser
        if self.displayHandTracking == True:
            frame = Image.fromarray(self.lm.latestFrame)
            frame = ImageTk.PhotoImage(image=frame)

            labelForFrame = tkinter.Label(image=frame)
            labelForFrame.image = frame
            labelForFrame.pack()

            labelForFrame.place(x=0, y=20)

        self.window.after(50, self.lm.recordCam)
        self.window.after(50, self.update)


    def displayVisualiser(self):
        if self.displayHandTracking == True:
            self.displayHandTracking = False
        else:
            self.displayHandTracking = True


window = App("HandUI", 600, 600)

print("")
print("Now running the configuration/visualisation mode of HandUI. Press \"CTRL + C\" into the terminal to exit.")
print("-------")
