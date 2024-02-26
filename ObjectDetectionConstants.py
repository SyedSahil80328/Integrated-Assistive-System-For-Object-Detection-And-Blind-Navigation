from cv2 import FONT_HERSHEY_PLAIN, FONT_HERSHEY_COMPLEX, FONT_HERSHEY_SCRIPT_SIMPLEX, FONT_HERSHEY_COMPLEX_SMALL, FONT_HERSHEY_TRIPLEX

knownDistance = 30  # Inches
knownWidth = 5.7  # Inches
thres = 0.5  # Threshold to detect object
nmsThreshold = 0.2  # (0.1 to 1) 1 means no suppress, 0.1 means high suppress

# Colors  >>> BGR Format(BLUE, GREEN, RED)
GREEN = (0, 255, 0)
RED = (0, 0, 255)
BLACK = (0, 0, 0)
YELLOW = (0, 255, 255)
WHITE = (255, 255, 255)
CYAN = (255, 255, 0)
MAGENTA = (255, 0, 242)
GOLDEN = (32, 218, 165)
LIGHT_BLUE = (255, 9, 2)
PURPLE = (128, 0, 128)
CHOCOLATE = (30, 105, 210)
PINK = (147, 20, 255)
ORANGE = (0, 69, 255)

font = FONT_HERSHEY_PLAIN
fonts = FONT_HERSHEY_COMPLEX
fonts2 = FONT_HERSHEY_SCRIPT_SIMPLEX
fonts3 = FONT_HERSHEY_COMPLEX_SMALL
fonts4 = FONT_HERSHEY_TRIPLEX

classNames = ["person", "bicycle", "car", "motorcycle", "airplane", "bus", "train", "truck", "boat", "traffic light", 
              "fire hydrant", "street sign", "stop sign", "parking meter", "bench", "bird", "cat", "dog", "horse", "sheep", "cow", 
              "elephant", "bear", "zebra", "giraffe", "hat", "backpack", "umbrella", "shoe", "eye glasses", "handbag", "tie", "suitcase", 
              "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat", "baseball glove", "skateboard", "surfboard", "tennis racket", 
              "bottle", "plate", "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli", 
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "couch", "plant", "bed", "mirror", "dining table", "window", 
              "desk", "toilet", "door", "tv", "laptop", "mouse", "remote", "keyboard", "cell phone", "microwave", "oven", "toaster", 
              "sink", "refrigerator", "blender", "book", "clock", "vase", "scissors", "teddy bear", "hair drier", "toothbrush", "hair brush"]
