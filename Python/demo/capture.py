# This file is just a demonstration of PoseNet, the code is not used in the project

import tensorflow as tf
import cv2

def initialize_posenet():
    # Setup TF Lite Interpreter
    interpreter = tf.lite.Interpreter(model_path="Pose Estimation Models\movenet.tflite")

    # Get input and output tensors
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    interpreter.allocate_tensors()

    return interpreter, (input_details, output_details)

# Function to predict keypoints
def keypoint_prediction(interpreter, model_details, input_img):
    interpreter.set_tensor(model_details[0][0]['index'], [input_img])
    interpreter.invoke()
    
    return interpreter.get_tensor(model_details[1][0]['index'])

capture = cv2.VideoCapture(0)
success, img = capture.read()

# Get original image dimensions
y, x, _ = img.shape

interpreter, model_details = initialize_posenet()

while success:
    # Resize image to the input size
    new_img = cv2.resize(img, (256, 256))

    keypoints = keypoint_prediction(interpreter, model_details, new_img)

    # Iterate through keypoints
    for keypoint in keypoints[0,0,:,:]:
        # Check confidence threshold
        if keypoint[2] > 0.5:
            # The first two channels of the last dimension represents the yx coordinates (normalized to image frame, i.e. range in [0.0, 1.0]) of the 17 keypoints
            yc = int(keypoint[0] * y)
            xc = int(keypoint[1] * x)

            # Draws a circle on the image for each keypoint
            img = cv2.circle(img, (xc, yc), 2, (128, 0, 128), 5)
    
    # Shows image
    cv2.imshow('Movenet', img)
    # Waits for the next frame, checks if q was pressed to quit
    if cv2.waitKey(1) == ord("q"):
        break

    # Reads next frame
    success, img = capture.read()

capture.release()
cv2.destroyAllWindows()