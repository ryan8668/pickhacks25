import zmq
import sys
import numpy as np
import cv2

import server.server as server
import pose_estimation.movenet as movenet

camera = cv2.VideoCapture(0)
success, img = camera.read()

socket = server.initialize_server()

interpreter, model_details = movenet.initialize_movenet("Pose Estimation Models\movenet.tflite")

while success:
    new_img = cv2.resize(img, (256, 256))
    keypoints = movenet.keypoint_prediction(interpreter, model_details, new_img)