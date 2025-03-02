import cv2
import platform

import server.server as server
import pose_estimation.movenet as movenet

camera = cv2.VideoCapture(0)
success, img = camera.read()

socket = server.initialize_server()

platform = str(platform.platform()).upper()
movenetPath = ""
if ("LINUX" in platform):
    movenetPath = "../../Pose Estimation Models/movenet.tflite"
else:
    movenetPath = "Pose Estimation Models\\movenet.tflite"

interpreter, model_details = movenet.initialize_movenet(movenetPath)

while success:
    new_img = cv2.resize(img, (256, 256))
    keypoints = movenet.keypoint_prediction(interpreter, model_details, new_img)