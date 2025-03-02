import zmq
import sys
import numpy as np

# Add pose_estimation to path
sys.path.insert(0, 'Python\pose_estimation')

# Setup ZMQ
def initialize_server():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")
    return socket

# Create array to store posenet data
keypoints = np.zeros((17, 3))

while True:
    message = socket.recv()
    
    socket.send(response)