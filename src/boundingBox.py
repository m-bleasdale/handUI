class BoundingBox:
    def __init__(self):
        self.minX = None
        self.maxX = None 
        self.minY = None 
        self.maxY = None

        self.center = None

    def checkAndUpdate(self, palmLandmark, frameHeight, frameWidth):

        #check for X coordinates
        if (self.minX is None) or (int(palmLandmark.x * frameWidth) < self.minX):
            self.minX = int(palmLandmark.x * frameWidth)
        if (self.maxX is None) or (int(palmLandmark.x * frameWidth) > self.maxX):
            self.maxX = int(palmLandmark.x * frameWidth)

        #check for Y coordinates
        if (self.minY is None) or (int(palmLandmark.y * frameHeight) < self.minY):
            self.minY = int(palmLandmark.y * frameHeight)
        if (self.maxY is None) or (int(palmLandmark.y * frameHeight) > self.maxY):
            self.maxY = int(palmLandmark.y * frameHeight)

    def determineCenter(self):
        
        midpointX = (self.maxX + self.minX) / 2
        midpointY = (self.maxY + self.minY) / 2

        self.center = [midpointX, midpointY]