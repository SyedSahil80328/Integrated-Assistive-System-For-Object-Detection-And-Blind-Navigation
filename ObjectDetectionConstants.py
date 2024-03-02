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

classNames = ["A person", "A bicycle", "A car", "A motorcycle", "An airplane", "A bus", "A train", "A truck", "A boat", "A traffic light", 
              "A fire hydrant", "A street sign", "A stop sign", "A parking meter", "A bench", "A bird", "A cat", "A dog", "A horse", "A sheep", "A cow", 
              "An elephant", "A bear", "A zebra", "A giraffe", "A hat", "A backpack", "An umbrella", "A shoe", "Eye glasses", "A handbag", "A tie", "A suitcase", 
              "A frisbee", "Skis", "A snowboard", "A sports ball", "A kite", "A baseball bat", "A baseball glove", "A skateboard", "A surfboard", "A tennis racket", 
              "A bottle", "A plate", "A wine glass", "A cup", "A fork", "A knife", "A spoon", "A bowl", "A banana", "An apple", "A sandwich", "An orange", "A broccoli", 
              "A carrot", "A hot dog", "A pizza", "A donut", "A cake", "A chair", "A couch", "A potted plant", "A bed", "A mirror", "A dining table", "A window", 
              "A desk", "A toilet", "A door", "A TV", "A laptop", "A mouse", "A remote", "A keyboard", "A cell phone", "A microwave", "An oven", "A toaster", 
              "A sink", "A refrigerator", "A blender", "A book", "A clock", "A vase", "Scissors", "A teddy bear", "A hair drier", "A toothbrush", "A hair brush"]
