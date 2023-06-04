import mediapipe as mp
import cv2
import numpy

from boundingBox import BoundingBox #boundingBox.py

class Landmarker:
    def __init__(self, displayHandTrackingFromStart):

        #values are read by other files
        self.latestFrame = None
        self.boxCenter = None 
        #frame dimensions
        self.frameWidth = None
        self.frameHeight = None
        #buffer zone dimensions
        self.bufferStart = None #top left of buffer zone
        self.bufferEnd = None #top right of buffer zone

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands()
        self.mp_draw = mp.solutions.drawing_utils

        self.cameraFootage = cv2.VideoCapture(0)

        self.displayHandTracking = displayHandTrackingFromStart



    #returns a blank frame
    def blankFrame(self, height, width):
        return numpy.zeros((height,width,3), numpy.uint8)


    #main function for getting landmarks
    def recordCam(self):

        streamOK, frame = self.cameraFootage.read()

        height, width, c = frame.shape

        self.frameWidth = width
        self.frameHeight = height

        #calculate buffer zone
        self.bufferStart = [
            round(height / 10), 
            round(width / 10)
        ]

        self.bufferEnd = [
            round(height - (height / 10)), 
            round(width - (width / 10))
        ]

        if streamOK:
            
            result = self.hands.process(frame)
            
            if result.multi_hand_landmarks:

                palmLandmarkIndexes = [0, 1, 5, 9, 13, 17]

                box = BoundingBox()

                #update bounding box points
                for palmLandmarkIndex in palmLandmarkIndexes:
                    palmLandmark = result.multi_hand_landmarks[0].landmark[palmLandmarkIndex]

                    box.checkAndUpdate(palmLandmark, height, width)

                #calculate center
                box.determineCenter()
                self.boxCenter = box.center

                
                if self.displayHandTracking == True:
                    #draw bounding box
                    cv2.rectangle(
                        frame, 
                        (box.minX, box.minY), 
                        (box.maxX, box.maxY), 
                        (0, 255, 0), 
                        2
                    )

                    #draw buffer zone
                    cv2.rectangle(
                        frame, 
                        (self.bufferStart[1], self.bufferStart[0]), 
                        (self.bufferEnd[1], self.bufferEnd[0]), 
                        (0, 0, 255),
                        2
                    )

                    #draw landmarks
                    for landmark in result.multi_hand_landmarks:
                        self.mp_draw.draw_landmarks(frame, landmark, self.mp_hands.HAND_CONNECTIONS)

                    #write center coordinates
                    cv2.putText(frame, f"{box.center[0]}, {box.center[1]}", (int(box.center[0]), int(box.center[1])), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)


                    #return latest frame
                    self.latestFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                    

                else:
                    #return blank frame
                    self.latestFrame = self.blankFrame(height,width)
            
            else:
                #return blank frame
                self.latestFrame = self.blankFrame(height,width)

                #reset box center
                self.boxCenter = None



