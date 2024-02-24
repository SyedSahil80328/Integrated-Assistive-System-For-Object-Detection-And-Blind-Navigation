from cv2 import cvtColor, COLOR_BGR2GRAY, line, CascadeClassifier, dnn_DetectionModel
from constants import GREEN, ORANGE, YELLOW

face_detector = CascadeClassifier("haarcascade_frontalface_default.xml")

import os

def set_audio_output(device_number):
    os.environ["PYGAME_DISPLAY"] = ":0"
    os.environ["SDL_AUDIODRIVER"] = "alsa"
    os.environ["SDL_AUDIODEV"] = f"hw:{device_number},0"

def setDetectionModel ():
    outputNet = dnn_DetectionModel("frozen_inference_graph.pb", "ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt") #Weightspath, Configpath
    outputNet.setInputSize(320, 320)
    outputNet.setInputScale(1.0 / 127.5)
    outputNet.setInputMean((127.5, 127.5, 127.5))
    outputNet.setInputSwapRB(True)
    
    return outputNet

# focal length finder function
def FocalLength(measured_distance, real_width, width_in_rf_image):
    focal_length = (width_in_rf_image * measured_distance) / real_width
    return focal_length

# distance estimation function
def Distance_finder(Focal_Length, real_face_width, face_width_in_frame):
    distance = (real_face_width * Focal_Length) / face_width_in_frame
    return distance

# face detection Function
def face_data(image, CallOut, Distance_level):
    face_width = 0
    face_x, face_y = 0, 0
    face_center_x = 0
    face_center_y = 0
    gray_image = cvtColor(image, COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray_image, 1.3, 5)
    for (x, y, h, w) in faces:
        LLV = int(h * 0.12)

        line(image, (x, y + LLV), (x + w, y + LLV), (GREEN), 2) #Fifth argument is thickness.
        line(image, (x, y + h), (x + w, y + h), (GREEN), 2)
        line(image, (x, y + LLV), (x, y + LLV + LLV), (GREEN), 2)
        line(image, (x + w, y + LLV), (x + w, y + LLV + LLV), (GREEN), 2)
        line(image, (x, y + h), (x, y + h - LLV), (GREEN), 2)
        line(image, (x + w, y + h), (x + w, y + h - LLV), (GREEN), 2)

        face_width = w
        face_center_x = int(w / 2) + x
        face_center_y = int(h / 2) + y

        if Distance_level < 10:
            Distance_level = 10

        if CallOut:
            line(image, (x, y - 11), (x + 180, y - 11), (ORANGE), 28)
            line(image, (x, y - 11), (x + 180, y - 11), (YELLOW), 20)
            line(image, (x, y - 11), (x + Distance_level, y - 11), (GREEN), 18)

    return face_width, faces, face_center_x, face_center_y
