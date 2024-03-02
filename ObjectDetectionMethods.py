from cv2 import cvtColor, COLOR_BGR2GRAY, line, CascadeClassifier, dnn_DetectionModel, VideoCapture
from ObjectDetectionConstants import GREEN, ORANGE, YELLOW
import socket

faceDetector = CascadeClassifier("IASCascadeClassifier.xml")

import os

def setAudioOutput(deviceNumber):
    os.environ["PYGAME_DISPLAY"] = ":0"
    os.environ["SDL_AUDIODRIVER"] = "alsa"
    os.environ["SDL_AUDIODEV"] = f"hw:{deviceNumber},0"

def setDetectionModel ():
    outputNet = dnn_DetectionModel("FrozenInferenceGraph.pb", "IASLargeCocoVersionThree.pbtxt") #Weightspath, Configpath
    outputNet.setInputSize(320, 320)
    outputNet.setInputScale(1.0 / 127.5)
    outputNet.setInputMean((127.5, 127.5, 127.5))
    outputNet.setInputSwapRB(True)
    
    return outputNet

def internetConnected():
    try:
        # Try connecting to Google's public DNS server
        socket.create_connection(("8.8.8.8", 53), timeout=5)
        return True
    except OSError:
        pass
    return False
    
def cameraConnected():
    capture = VideoCapture(0)
    if not capture.isOpened():
        return False
    return True

# focal length finder function
def focalLength(measuredDistance, realWidth, widthInRfImage):
    focalLength = (widthInRfImage * measuredDistance) / realWidth
    return focalLength

# distance estimation function
def distanceFinder(focalLength, realFaceWidth, faceWidthInFrame):
    distance = (realFaceWidth * focalLength) / faceWidthInFrame
    return distance

# face detection Function
def faceData(image, callOut, distanceLevel):
    faceWidth = 0
    faceX, faceY = 0, 0
    faceCenterX = 0
    faceCenterY = 0
    grayImage = cvtColor(image, COLOR_BGR2GRAY)
    faces = faceDetector.detectMultiScale(grayImage, 1.3, 5)
    for (x, y, h, w) in faces:
        LLV = int(h * 0.12)

        line(image, (x, y + LLV), (x + w, y + LLV), (GREEN), 2) #Fifth argument is thickness.
        line(image, (x, y + h), (x + w, y + h), (GREEN), 2)
        line(image, (x, y + LLV), (x, y + LLV + LLV), (GREEN), 2)
        line(image, (x + w, y + LLV), (x + w, y + LLV + LLV), (GREEN), 2)
        line(image, (x, y + h), (x, y + h - LLV), (GREEN), 2)
        line(image, (x + w, y + h), (x + w, y + h - LLV), (GREEN), 2)

        faceWidth = w
        faceCenterX = int(w / 2) + x
        faceCenterY = int(h / 2) + y

        if distanceLevel < 10:
            distanceLevel = 10

        if callOut:
            line(image, (x, y - 11), (x + 180, y - 11), (ORANGE), 28)
            line(image, (x, y - 11), (x + 180, y - 11), (YELLOW), 20)
            line(image, (x, y - 11), (x + distanceLevel, y - 11), (GREEN), 18)

    return faceWidth, faces, faceCenterX, faceCenterY
