import numpy as np
import cv2
from scipy.spatial import distance as dist
import pyttsx3

from ObjectDetectionConstants import *
from ObjectDetectionMethods import *

# Camera Object
# cap = cv2.VideoCapture(0, cv2.CAP_V4L2) # For RPI
cap = cv2.VideoCapture(0)  # For Laptop or Desktop
faceModel = cv2.CascadeClassifier('IASCascadeClassifier.xml')
distanceLevel = 0
colors = np.random.uniform(0, 255, size=(len(classNames), 3))

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('output21.mp4', fourcc, 30.0, (640, 480))
out = cv2.VideoWriter('output21.avi', fourcc, 30.0, (640, 480))

net = setDetectionModel()

# reading reference image from directory
refImage = cv2.imread("Face.png")
refImageFaceWidth, _, _, _ = faceData(refImage, False, distanceLevel)
focalLengthFound = focalLength(knownDistance, knownWidth, refImageFaceWidth)
print(focalLengthFound)

setAudioOutput(1)

# Initialize the text-to-speech engine
engine = pyttsx3.init()

while True:
    _, frame = cap.read()

    classIds, confs, bbox = net.detect(frame, confThreshold=thres)

    bbox = list(bbox)
    confs = list(np.array(confs).reshape(1, -1)[0])
    confs = list(map(float, confs))
    indices = cv2.dnn.NMSBoxes(bbox, confs, thres, nmsThreshold)

    faceWidthInFrame, faces, fcX, fcY = faceData(frame, True, distanceLevel)

    if len(classIds) != 0:
        for i in indices:
            box = bbox[i]
            confidence = str(round(confs[i], 2))
            color = colors[classIds[i] - 1]
            x, y, w, h = box[0], box[1], box[2], box[3]
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, thickness=2)
            cv2.putText(frame, classNames[classIds[i] - 1] + " " + confidence, (x + 10, y + 20),
                        font, 1, color, 2)

    for (faceX, faceY, faceW, faceH) in faces:
        if faceWidthInFrame != 0:
            distance = distanceFinder(focalLengthFound, knownWidth, faceWidthInFrame)
            distance = round(distance, 2)
            
            if len(classIds) > 0 and 0 <= i < len(classIds):
                if 10 < distance < 50:
                    objectName = classNames[classIds[i] - 1]
                    engine.say(f"Move Away from {objectName}")
                    engine.runAndWait()
                elif distance >= 50:
                    engine.stop()

            distanceLevel = int(distance)
            cv2.putText(frame, f"Distance {distance} Inches",
                        (faceX - 6, faceY - 6), fonts, 0.5, (BLACK), 2)

    if cv2.waitKey(1) == ord("q"):
        break

    status, photo = cap.read()
    l = len(bbox)
    frame = cv2.putText(frame, str(len(bbox)) + " Object", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2,
                        cv2.LINE_AA)
    stackX = []
    stackY = []
    stackXPrint = []
    stackYPrint = []
    global D

    if len(bbox) == 0:
        pass
    else:
        for i in range(0, len(bbox)):
            x1 = bbox[i][0]
            y1 = bbox[i][1]
            x2 = bbox[i][0] + bbox[i][2]
            y2 = bbox[i][1] + bbox[i][3]

            midX = int((x1 + x2) / 2)
            midY = int((y1 + y2) / 2)
            stackX.append(midX)
            stackY.append(midY)
            stackXPrint.append(midX)
            stackYPrint.append(midY)

            frame = cv2.circle(frame, (midX, midY), 3, [0, 0, 255], -1)
            frame = cv2.rectangle(frame, (x1, y1), (x2, y2), [0, 0, 255], 2)

        if len(bbox) == 2:
            D = int(dist.euclidean((stackX.pop(), stackY.pop()), (stackX.pop(), stackY.pop())))
            frame = cv2.line(frame, (stackXPrint.pop(), stackYPrint.pop()),
                             (stackXPrint.pop(), stackYPrint.pop()), [0, 0, 255], 2)
        else:
            D = 0

        if D < 250 and D != 0:
            frame = cv2.putText(frame, "!!MOVE AWAY!!", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, [0, 0, 255], 4)
            objectName = classNames[classIds[i] - 1]
            engine.say(f"Move Away from {objectName}")
            engine.runAndWait()
        elif D >= 250:
                engine.stop()

        frame = cv2.putText(frame, str(D / 10) + " cm", (300, 50), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (255, 0, 0), 2, cv2.LINE_AA)

        cv2.imshow('Output', frame)
        if cv2.waitKey(100) == 13:
            break

cap.release()
cv2.destroyAllWindows()
