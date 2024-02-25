import numpy as np
import cv2
from scipy.spatial import distance as dist
import pyttsx3

from constants import *
from methods import *

# Camera Object
cap = cv2.VideoCapture(0)  # Number According to Camera
#cap = cv2.VideoCapture("rtsp://admin:admin@192.168.198.185:1935")  # Number According to Camera
face_model = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
Distance_level = 0
Colors = np.random.uniform(0, 255, size=(len(classNames), 3))

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('output21.mp4', fourcc, 30.0, (640, 480))
out = cv2.VideoWriter('output21.avi', fourcc, 30.0, (640, 480))
 
net = setDetectionModel();

# reading reference image from directory
ref_image = cv2.imread("face.png")
ref_image_face_width, _, _, _ = face_data(ref_image, False, Distance_level)
Focal_length_found = FocalLength(Known_distance, Known_width, ref_image_face_width)
print(Focal_length_found)

set_audio_output(1)

# Initialize the text-to-speech engine
engine = pyttsx3.init()

while True:
    _, frame = cap.read()

    classIds, confs, bbox = net.detect(frame, confThreshold=thres)

    bbox = list(bbox)
    confs = list(np.array(confs).reshape(1, -1)[0])
    confs = list(map(float, confs))
    indices = cv2.dnn.NMSBoxes(bbox, confs, thres, nms_threshold)

    face_width_in_frame, Faces, FC_X, FC_Y = face_data(frame, True, Distance_level)

    if len(classIds) != 0:
        for i in indices:
            box = bbox[i]
            confidence = str(round(confs[i], 2))
            color = Colors[classIds[i] - 1]
            x, y, w, h = box[0], box[1], box[2], box[3]
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, thickness=2)
            cv2.putText(frame, classNames[classIds[i] - 1] + " " + confidence, (x + 10, y + 20),
                        font, 1, color, 2)

    for (face_x, face_y, face_w, face_h) in Faces:
        if face_width_in_frame != 0:
            Distance = Distance_finder(Focal_length_found, Known_width, face_width_in_frame)
            Distance = round(Distance, 2)
            
            if len(classIds) > 0 and 0 <= i < len(classIds):
                if 10 < Distance < 50:
                    engine.say(f"Move Away from {classNames[classIds[i] - 1]}")
                    engine.runAndWait()
                elif Distance >= 50:
                    engine.stop()

            Distance_level = int(Distance)
            cv2.putText(frame, f"Distance {Distance} Inches",
                        (face_x - 6, face_y - 6), fonts, 0.5, (BLACK), 2)

    if cv2.waitKey(1) == ord("q"):
        break

    status, photo = cap.read()
    l = len(bbox)
    frame = cv2.putText(frame, str(len(bbox)) + " Object", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2,
                        cv2.LINE_AA)
    stack_x = []
    stack_y = []
    stack_x_print = []
    stack_y_print = []
    global D

    if len(bbox) == 0:
        pass
    else:
        for i in range(0, len(bbox)):
            x1 = bbox[i][0]
            y1 = bbox[i][1]
            x2 = bbox[i][0] + bbox[i][2]
            y2 = bbox[i][1] + bbox[i][3]

            mid_x = int((x1 + x2) / 2)
            mid_y = int((y1 + y2) / 2)
            stack_x.append(mid_x)
            stack_y.append(mid_y)
            stack_x_print.append(mid_x)
            stack_y_print.append(mid_y)

            frame = cv2.circle(frame, (mid_x, mid_y), 3, [0, 0, 255], -1)
            frame = cv2.rectangle(frame, (x1, y1), (x2, y2), [0, 0, 255], 2)

        if len(bbox) == 2:
            D = int(dist.euclidean((stack_x.pop(), stack_y.pop()), (stack_x.pop(), stack_y.pop())))
            frame = cv2.line(frame, (stack_x_print.pop(), stack_y_print.pop()),
                             (stack_x_print.pop(), stack_y_print.pop()), [0, 0, 255], 2)
        else:
            D = 0

        if D < 250 and D != 0:
            frame = cv2.putText(frame, "!!MOVE AWAY!!", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, [0, 0, 255], 4)
            engine.say(f"Move Away from object")
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
