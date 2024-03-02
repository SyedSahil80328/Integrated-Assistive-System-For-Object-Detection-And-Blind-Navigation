import numpy as np
import cv2
from scipy.spatial import distance as dist
import pyttsx3

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import threading
import time

from ObjectDetectionConstants import *
from ObjectDetectionMethods import *

#Sender's email credentials
senderEmail = "Your Sender Email ID"
senderPassword = "Your 16 Digit App Password"

# Receiver's email
receiverEmail = "Your Receiver Email ID"

# Create the message
subject = "Raspberry PI Blind Support"
body = "Hi. I am SAM. I will send mail to share live locations your client is currently at."

# Initialize the text-to-speech engine
engine = pyttsx3.init()

rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 125)  # reducing the rate to 125 units

def detectObject():
    while not cameraConnected():
        print("Camera is not connected.")
        time.sleep(5)
    
    print("Successfully connected the camera.")
    
    # Camera Object
    # cap = cv2.VideoCapture(0, cv2.CAP_V4L2) # For RPI
    cap = cv2.VideoCapture(0)  # For Laptop or Desktop
    faceModel = cv2.CascadeClassifier('IASCascadeClassifier.xml')
    distanceLevel = 0
    colors = np.random.uniform(0, 255, size=(len(classNames), 3))
    
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    #out = cv2.VideoWriter('OutputVideo.mp4', fourcc, 30.0, (640, 480))
    out = cv2.VideoWriter('OutputVideo.avi', fourcc, 30.0, (640, 480))
    
    net = setDetectionModel()
    
    # reading reference image from directory
    refImage = cv2.imread("Face.png")
    refImageFaceWidth, _, _, _ = faceData(refImage, False, distanceLevel)
    focalLengthFound = focalLength(knownDistance, knownWidth, refImageFaceWidth)
    print(focalLengthFound)
    
    setAudioOutput(1)
    
    engine.say(f"Hi! I'm SAM, your companion. I'm here to guide you for safe journey.")
    print(f"Hi! I'm SAM, your companion. I'm here to guide you for safe journey.")
    
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
                        engine.say(f"{classNames[classIds[i] - 1]} is {round(distance)} inches in front of you.")
                        print(f"{classNames[classIds[i] - 1]} is {round(distance)} inches in front of you.")
                        engine.runAndWait()
                    elif Distance >= 50:
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
        global d
    
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
                d = int(dist.euclidean((stackX.pop(), stackY.pop()), (stackX.pop(), stackY.pop())))
                frame = cv2.line(frame, (stackXPrint.pop(), stackYPrint.pop()),
                                 (stackXPrint.pop(), stackYPrint.pop()), [0, 0, 255], 2)
            else:
                d = 0
    
            if d < 250 and d != 0:
                frame = cv2.putText(frame, "!!MOVE AWAY!!", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, [0, 0, 255], 4)
                cv2.FONT_HERSHEY_SIMPLEX, 2, [0, 0, 255], 4)
                engine.say(f"There is {classNames[classIds[i] - 1]} in front of you. Be cautious.")
                engine.runAndWait()
            elif d >= 250:
                    engine.stop()
    
            frame = cv2.putText(frame, str(d / 10) + " cm", (300, 50), cv2.FONT_HERSHEY_SIMPLEX,
                                1, (255, 0, 0), 2, cv2.LINE_AA)
    
            cv2.imshow('Output', frame)
            if cv2.waitKey(100) == 13:
                break
    
    cap.release()
    cv2.destroyAllWindows()

def sendEmail():
    while not internetConnected():
        print("No internet connection.")
        time.sleep(5)
    
    print("Internet is connected.")
    while True:
        # Create a new message for each iteration
        try:
            message = MIMEMultipart()
            message['From'] = senderEmail
            message['To'] = receiverEmail
            message['Subject'] = subject
            message.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()

                # Login to the sender's email account
                server.login(senderEmail, senderPassword)

                # Send the email
                server.sendmail(senderEmail, receiverEmail, message.as_string())

            print("Email sent successfully!")

            # Wait for 30 seconds before sending the next email
            time.sleep(30)
        except Exception as e:
            print("Internet is Disconnected.")
            time.sleep(10)
        
# Start the email thread
emailThread = threading.Thread(target=sendEmail)
emailThread.start()

# Start the video capture and display thread
videoThread = threading.Thread(target=detectObject)
videoThread.start()

# Wait for both threads to finish
emailThread.join()
videoThread.join()
