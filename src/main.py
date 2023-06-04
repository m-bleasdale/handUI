from landmarker import Landmarker;
import cursorController


print("HandUI is loading. Please wait...")



lm = Landmarker(False)



print("")
print("Now running HandUI. Press \"CTRL + C\" into the terminal to exit.")
print("Run \"app.py\" to see the tracking visualiser.")
print("-------")



try:

    continueLoop = True

    while continueLoop:

        lm.recordCam()

        if lm.boxCenter != None:

            position = cursorController.calculatePositionOnScreen(lm)

            cursorController.moveCursor(position)

        
#close program
except KeyboardInterrupt:

    print("Successfully closed HandUI")




