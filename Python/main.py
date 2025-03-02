import cv2
import platform
import socket
import json

import pose_estimation.movenet as movenet

HOST = '127.0.0.1'
PORT = 5555

camera = cv2.VideoCapture(0)
success, img = camera.read()

platform = str(platform.platform()).upper()
movenetPath = ""
if ("LINUX" in platform):
    movenetPath = "../Pose Estimation Models/movenet.tflite"
else:
    movenetPath = "Pose Estimation Models\\movenet.tflite"

interpreter, model_details = movenet.initialize_movenet(str(movenetPath))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    print(f"Server listening on {HOST}:{PORT}")

    conn, addr = server.accept()

    with conn:
        print('Connected by', addr)
        while True:
            new_img = cv2.resize(img, (256, 256))
            data = movenet.keypoint_prediction(interpreter, model_details, new_img).reshape(17,3)
            
            # Send JSON data with a newline delimiter
            conn.sendall((str(data) + "\n").encode('utf-8'))

            success, img = camera.read()

            if not success:
                print("Failed to read from camera")
                break

camera.release()