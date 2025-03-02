import cv2
import platform
import zmq
import json

import pose_estimation.movenet as movenet

camera = cv2.VideoCapture(0)
success, img = camera.read()

context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.bind("tcp://*:5555")

platform = str(platform.platform()).upper()
movenetPath = ""
if ("LINUX" in platform):
    movenetPath = "../../Pose Estimation Models/movenet.tflite"
else:
    movenetPath = "Pose Estimation Models\\movenet.tflite"

interpreter, model_details = movenet.initialize_movenet(movenetPath)

while True:
    success, img = camera.read()
    if not success:
        print("Failed to read from camera")
        break

    new_img = cv2.resize(img, (256, 256))
    keypoints = movenet.keypoint_prediction(interpreter, model_details, new_img)

    socket.send_json(json.dumps(keypoints.tolist()))