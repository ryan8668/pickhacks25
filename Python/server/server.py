import zmq
import numpy as np
import Python.pose_estimation.posenet as posenet
import Python.server.client_comand_handling as client_comand_handling

# Setip ZMQ
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

posenet.initialize_posenet()

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
        keypoints = posenet.keypoint_prediction(img).reshape(17, 3)
    else:
        response = b"Invalid message size"
    
    socket.send(response)