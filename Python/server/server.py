import zmq
import sys
import numpy as np
import client_comand_handling

# Add pose_estimation to path
sys.path.insert(0, 'Python\pose_estimation')
import movenet

# Setup ZMQ
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

movenet.initialize_posenet("Pose Estimation Models\movenet.tflite")

# Create array to store posenet data
keypoints = np.zeros((17, 3))

while True:
    message = socket.recv()

    # Check if the message is a command or an image
    if len(message) < 256:
        # Process command
        response = client_comand_handling.proccess_command(message)
    elif len(message) == 256 * 256 * 3:
        # Convert to correct size tensor
        img = np.array(message, dtype=np.uint8).reshape(256, 256, 3)

        # Make prediction
        keypoints = movenet.keypoint_prediction(img).reshape(17, 3)
        response = keypoints.tobytes()
    else:
        response = b"Invalid message size"
    
    socket.send(response)