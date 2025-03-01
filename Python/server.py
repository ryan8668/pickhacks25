import zmq
import numpy as np
import posenet


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

posenet.initialize_posenet()

keypoints = np.zeros((17, 3))

while True:
    message = socket.recv()

    # Check vaild message size
    if len(message) == 256 * 256 * 3:
        #Convert to correct size tensor
        img = np.array(message, dtype=np.uint8).reshape(256, 256, 3)

        # Make prediction
        keypoints = posenet.keypoint_prediction(img).reshape(17, 3)
    
    socket.send(keypoints.tobytes())