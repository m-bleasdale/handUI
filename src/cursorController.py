import pyautogui

class CursorPosition:
    def __init__(self, handPosition, screenDimension, frameDimension, bufferDimension):

        positionMultiplier = (handPosition - bufferDimension) / (frameDimension * 0.9)

        self.coordinate = screenDimension * positionMultiplier



def calculatePositionOnScreen(landmarkObject):

    screenWidth, screenHeight = pyautogui.size()

    cursorPosition_X = CursorPosition(landmarkObject.boxCenter[0], screenWidth, landmarkObject.frameWidth, landmarkObject.bufferStart[1])
    cursorPosition_Y = CursorPosition(landmarkObject.boxCenter[1], screenHeight, landmarkObject.frameHeight, landmarkObject.bufferStart[0])

    #rounded to nearest pixel(integer)
    return [
        round(cursorPosition_X.coordinate), 
        round(cursorPosition_Y.coordinate)
    ]

def moveCursor(position):
    pyautogui.FAILSAFE = False

    pyautogui.moveTo(position[0], position[1], duration=0)